from fabric.contrib.console import confirm
from fabric.contrib.files import append, exists, sed, put
from fabric.api import env, local, run, sudo
from fabric.colors import green, red

import os
import json

from fabric.utils import abort


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))  # ceosProject (remote에선 Veeto)
BASE_DIR = os.path.dirname(PROJECT_DIR)

with open(os.path.join(PROJECT_DIR, "deploy.json")) as f:
    envs = json.loads(f.read())

REPO_URL = envs['REPO_URL']
REPO_NAME = envs['REPO_NAME']
PROJECT_NAME = envs['PROJECT_NAME']
REMOTE_HOST_SSH = envs['REMOTE_HOST_SSH']
REMOTE_HOST = envs['REMOTE_HOST']
REMOTE_USER = envs['REMOTE_USER']

env.user = REMOTE_USER
username = env.user
env.hosts = [REMOTE_HOST_SSH, ]
env.key_filename = ["~/.ssh/aws_ec2_heejoe0222.pem",]

project_folder = '/home/{}/srv/{}'.format(env.user, REPO_NAME)
virtualenv_folder = '/home/{}/.pyenv/versions/production'.format(env.user)
app1 = 'accounts'
app2 = 'main'
local_project_folder = os.path.join(PROJECT_DIR, PROJECT_NAME)


def _check_if_migration_needed(skip_migrations=False):
    if skip_migrations:
        return

    result = local('./manage.py makemigrations --dry-run', capture=True)

    if result.stdout != 'No changes detected' and not confirm(
            red("FAIL: Some model change found. You need to run makemigrations. \nOr just continue anyway?")):
        print(red('\n\t'.join(result.stdout.strip().split('[ ]'))))
        print(red(
            "Please apply migrations with 'python manage.py migrate'\n\n"
            "If you want to skip them, execute it with 'fab deploy:skip_migrations=True'\n"
            "For doing this, please check if migrations are committed in remote VCS."
            "If so, it will be applied to your remote machine."))
        raise SystemExit

def _local_test():
    result = local('./manage.py test --keepdb'.format(PROJECT_DIR), capture=True)
    if result.failed and not confirm("FAIL: Local tests are failed.\nContinue anyway?"):
        abort("Aborting at user request.")

def _get_latest_source():
    print(green('_get_latest_source'))
    if exists(project_folder + '/.git'):
        run('cd {} && git fetch'.format(project_folder, ))
    else:
        run('git clone {} {}'.format(REPO_URL, project_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd {} && git reset --hard {}'.format(project_folder, current_commit))

def _upload_secrets_file():
    print(green('_upload_secrets_file'))
    secret_file_dir = os.path.join(local_project_folder, 'secrets.json')
    remote_project_setting_dir = '{}@{}:{}'.format(REMOTE_USER, REMOTE_HOST_SSH,
                                                   os.path.join(project_folder, PROJECT_NAME))
    local('scp {} {}'.format(secret_file_dir, remote_project_setting_dir))

def _update_settings():
    print(green('_update_settings'))
    settings_path = project_folder + '/{}/settings/__init__.py'.format(PROJECT_NAME)
    sed(settings_path, "dev", "prod")

def _update_virtualenv():
    print(green('_update_virtualenv'))
    run('{}/bin/pip install -r {}/requirements.txt'.format(virtualenv_folder, project_folder))

def _update_static_files():  # 수정해야
    print(green('_update_static_files'))
    run('sudo chown -R ubuntu:ubuntu /srv/{}/.static_root').format(REPO_NAME)
    run('cd {} && {}/bin/python3 manage.py collectstatic --noinput'.format(project_folder, virtualenv_folder))
    run('sudo chown -R root:root /srv/{}/.static_root').format(REPO_NAME)

def _update_database():
    print(green('_update_database'))
    run('cd {} && {}/bin/python3 manage.py makemigrations --noinput'.format(project_folder, virtualenv_folder))
    run('cd {} && {}/bin/python3 manage.py migrate --noinput'.format(project_folder, virtualenv_folder))
    run('cd {} && {}/bin/python3 manage.py makemigrations {} --noinput'.format(project_folder, virtualenv_folder,
                                                                               app1))
    run('cd {} && {}/bin/python3 manage.py migrate {} --noinput'.format(project_folder, virtualenv_folder, app1))
    run('cd {} && {}/bin/python3 manage.py makemigrations {} --noinput'.format(project_folder, virtualenv_folder,
                                                                               app2))
    run('cd {} && {}/bin/python3 manage.py migrate {} --noinput'.format(project_folder, virtualenv_folder, app2))

def _run_django_test():
    result = run('cd {} && {}/bin/python3 manage.py test --keepdb --failfast'.format(project_folder, virtualenv_folder))
    if result.failed:
        print(red("Some tests failed"))
        raise SystemExit
    else:
        print(green("All tests passed!"))

def _grant_uwsgi():
    print(green('_grant_uwsgi'))
    sudo('sudo chown -R :deploy {}'.format(project_folder))

def _restart_uwsgi():
    print(green('_restart_uwsgi'))
    sudo('sudo cp -f {}/conf/uwsgi/uwsgi.service /etc/systemd/system/uwsgi.service'.format(project_folder))
    sudo('sudo systemctl daemon-reload')
    sudo('sudo systemctl restart uwsgi')

def _restart_nginx():
    print(green('_restart_nginx'))
    sudo('sudo cp -f {}/conf/nginx/nginx.conf /etc/nginx/sites-available/veeto.conf'.format(project_folder))
    sudo('sudo ln -sf /etc/nginx/sites-available/veeto.conf /etc/nginx/sites-enabled/veeto.conf')
    sudo('sudo systemctl restart nginx')

## fab 명령어로 실행하기
def deploy(skip_migration=False):
    #_check_if_migration_needed(skip_migration)
    #_local_test()
    try:
        _get_latest_source()
        _upload_secrets_file()
        _update_settings()
        _update_virtualenv()
        _update_static_files()
        _update_database()
        _run_django_test()
        _grant_uwsgi()
        _restart_uwsgi()
        _restart_nginx()

    except SystemExit as e:
        print("Deploy failed!!")

def refresh():
    _grant_uwsgi()
    _restart_uwsgi()
    _restart_nginx()