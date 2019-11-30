from django.db import models
#from django.contrib.auth.models import PermissionsMixin
#from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class University(models.Model):
    school_name = models.CharField(max_length=15)

    def __str__(self):
        return self.school_name


class registerForm(models.Model):
    user_name = models.CharField(max_length=10)
    user_nickname = models.CharField(max_length=5) #unique=True
    age = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    phone_num = models.CharField(max_length=11) #unique=True
    studentCard_image = models.ImageField(upload_to='auth/', null=False)
    university_auth = models.BooleanField(default=False) #학교 인증했는지 여부

    desired_room = models.ForeignKey('main.RoomCandidate', on_delete=models.PROTECT) #원하는 방 종류
    desired_gender_ratio = models.IntegerField(verbose_name="희망 성비") #동성 1, 1:1 2, 무관 3


class TempUser(models.Model):
    user_name = models.CharField(max_length=10)
    user_nickname = models.CharField(max_length=5) #unique=True
    age = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    phone_num = models.CharField(max_length=11) #unique=True


'''
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id, password, **extra_fields):
        if not user_id :
            raise ValueError('아이디는 필수 요소입니다.')
        if not password :
            raise ValueError('패스워드는 필수 요소입니다.')
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, password, **extra_fields)

    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff',True)
        return self._create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=15, null=True)  # unique=True
    date_of_birth = models.DateField(null=True)  # age  # 관리자만 null 가능
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')

    user_id = models.CharField(max_length=20, unique=True)
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)  # 관리자만 null 가능
    school_email = models.EmailField(blank=True)

    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/uploads', default='profiles/jordy.jpg')
    self_pr = models.CharField(max_length=50, default="#이런사람") # 해시태그로 자기소개
    university_auth = models.BooleanField(default=False) #학교 인증했는지 여부
    beans = models.IntegerField(default=0)  # 서비스 가상화폐


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # 계정 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 계정 수정일

    objects = UserManager()

    USERNAME_FIELD = 'user_id'

    def __str__(self):
        return self.username

    def get_id(self):
        return self.user_id

    def get_age(self):
        today = date.today()
        return today.year-self.date_of_birth.year+1
'''
