import datetime
from django.db import models

# Create your models here.

class User(models.Model):
    '''用户信息模型 '''
    SEX = (
        ('M', '男'),
        ('F', '女'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)

    birth_year = models.CharField()
    birth_month = models.CharField()
    birth_day = models.CharField()

    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property # 可以把当前的函数变成一个只读的属性.
    def age(self):
        today = datetime.date.today() 
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_date).days // 365


class Profile(models.Model):
    '''用户配置模型'''

    SEX = (
        ('M', '男'),
        ('F', '女'),
    )

    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1)
    max_distance = models.IntegerField(default=10)

    min_dating_age = models.IntegerField(default=18)
    min_dating_age = models.IntegerField(default=45)

    dating_sex = models.CharField(max_length=8, choices=SEX)
    
    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')

    only_mathce = models.BooleanField(default=True, verbose_name='不让为匹配的人看我相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')