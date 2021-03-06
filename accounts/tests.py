import tempfile

from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from accounts.models import University

from io import StringIO
from PIL import Image
from django.core.files.base import File


# Create your tests here.

class TestFileUpload(APITestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(school_name="이화여대");
        pass

    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        # image.save(name, ext)
        # file_obj.seek(0)
        image = Image.new("RGBA", size=size, color=color)
        return File(image, name=name)

    '''
    def test_file_is_accepted(self):
        url = reverse('accounts:register-user-form')
        image = open('C:\\Users\\heejo\\Pictures\\universe.jpg','rb')
        data = {
            'user_name':'heejoe',
            'user_nickname' : 'dev',
            'age' : 22,
            'university' : 1, # universiry model - foreign key
            'gender' : 'F',
            'phone_num' : '01022222222',
            'studentCard_image': image,
            'desired_gender_ratio' : 3,
            'date': '2019-12-22',
            'activity': 2,
            'time': '19:00'
        }

        response = self.client.post( url, data, format='multipart')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    '''

    def test_image_only_is_accepted(self):
        url = reverse('accounts:user-auth')
        # image = self.get_image_file()
        #
        # image = Image.new('RGB', (100, 100))
        # tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        # image.save(tmp_file)
        # tmp_file.seek(0)


        with open('C:\\Users\\heejo\\Pictures\\mvp_wireframe.png','rb') as fp:
            response = self.client.post(url, data = {'image': fp}, format='multipart')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

