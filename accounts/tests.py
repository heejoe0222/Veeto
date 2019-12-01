# from rest_framework import status
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from accounts.models import University
#
# # Create your tests here.
#
# class TestFileUpload(APITestCase):
#
#     def test_file_is_accepted(self):
#         url = reverse('accounts:register-user-form')
#         image = open('C:\\Users\\heejo\\Pictures\\universe.jpg','rb')
#         data = {
#             'user_name':'heejoe',
#             'user_nickname' : 'dev',
#             'age' : 22,
#             'university' : 1,
#             'gender' : 'F',
#             'phone_num' : '01022222222',
#             'studentCard_image': image,
#             'desired_gender_ratio' : 3,
#             'date': '2019-12-22',
#             'activity': 2,
#             'time': '19:00'
#         }
#
#         response = self.client.post( url, data, format='multipart')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
