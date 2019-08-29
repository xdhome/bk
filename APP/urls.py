from django.conf.urls import url
from .views import *


urlpatterns = [
    # 登录
    url(r'login/$', login, name='login')
]