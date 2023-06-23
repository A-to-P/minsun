from django.contrib import admin
from .models import Blog #블로그 모델 사용 
# Register your models here.

admin.site.register(Blog)  #admin에 블로그 모델 알려주기 
