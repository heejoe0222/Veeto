from django.db import models


class University(models.Model):
    school_name = models.CharField(max_length=15)

    def __str__(self):
        return self.school_name


# mvp 구현을 위한 임시 모델 -> 이후 USER 클래스 상속 예정
class SimpleUser(models.Model):
    user_name = models.CharField(max_length=10)
    age = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    major = models.CharField(max_length=50, default="전공미입력")  # not null로 바꿀수도
    self_pr = models.CharField(max_length=50, default="#이런사람") # 해시태그로 자기소개
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M','Male'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='F')

    def __str__(self):
        return self.user_name
