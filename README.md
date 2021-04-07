# swiper
a python project django.

# git 的使用

```shell
# create ssh key
ssh-keygen 

# github -> settting -> ssh setting
git clone ssh@..


# 安装虚拟环境 venv
python -m venv .venv

# 吧所有安装的库输入到文件
pip freeze > requirements.txt

# pip 软件
pip install -r requirements.txt

git add . # 提交所有文件

git commit -m 'commit text'

git push # 提交到远程服务器
```

# Django 创建项目

```python 
python -m pip install django

django-admin startproject [项目名称]

django-admin startapp [模块]

./manage.py shell # 直接进入 Django 环境,避免有模块没有导入.

# 数据库迁移 shell
python manage.py makemigrations

python manage.py migrate
```

# celery 