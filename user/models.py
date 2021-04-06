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

    birth_year = models.CharField(max_length=8)
    birth_month = models.CharField(max_length=8)
    birth_day = models.CharField(max_length=8)

    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property # 可以把当前的函数变成一个只读的属性.
    def age(self):
        today = datetime.date.today() 
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_date).days // 365

    @property
    def profile(self):
        '''用户的配置; 分布式'''
        if not hasattr(self, '_profile'):
            _profile, _ = Profile.objects.get_or_create(id=self.id)
            self._profile = _profile
        return self._profile


class Profile(models.Model):
    '''用户配置模型'''

    SEX = (
        ('M', '男'),
        ('F', '女'),
    )

    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最短距离')
    max_distance = models.IntegerField(default=10, verbose_name='最长距离')

    min_dating_age = models.IntegerField(default=18, verbose_name='最小年龄')
    min_dating_age = models.IntegerField(default=45, verbose_name='最大年龄')

    dating_sex = models.CharField(efault='F', choices=SEX, verbose_name='对方性别.')
    
    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')

    only_mathce = models.BooleanField(default=True, verbose_name='不让为匹配的人看我相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')