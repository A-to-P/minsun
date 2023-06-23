from django.urls import path
from .views import *  

app_name = 'user'  #user 앱 이름 명시-> user: 로 이용

urlpatterns = [
    # USER
    path('signup/', signup, name='signup'), # 회원가입
    path('signin/', signin, name='signin'), # 로그인 
    path('signout/', signout, name='signout'), # 로그아웃
    
    # PROFILE 
    path('new_profile/', new_profile, name='new_profile'), # 새 프로필 만드는 창  
    path('create_profile/', create_profile, name='create_profile'),  # 프로필 생성 작업 

    
    ]
