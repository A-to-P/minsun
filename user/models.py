from django.db import models
# 장고 기본 제공
# from django.contrib.auth.models import User

# 커스텀
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


# AbstractBaseUser로 CustomUser 만들면 CustomUserManager로 관리
# 커스텀 위해 UserManager을 대신 BaseUserManager 사용

# 커스텀 유저 매니저 (관리자)
class CustomUserManager(BaseUserManager):
  # 유저 생성 기본 함수 
  def create_user(self, username,email, password, **kwargs):  # username, password, 기타(딕셔너리형)을 파라미터로 받는다. 
    if not username:
      raise ValueError("must have user name!!")
    if not email:
      raise ValueError("must have user email!!")
    
    user = self.model(username=username, email=self.normalize_email(email), **kwargs) 
    user.set_password(username=username, **kwargs) 
    user.save() #db에 저장
  
  # 일반 유저 생성 
  def create_normaluser(self, username,email, password, **kwargs):
    self.create_user(username, email , password,**kwargs) 
  
  # 슈퍼 유저 생성
  def create_superuser(self, username,email, password, **kwargs):
    kwargs.setdefault("is_superuser", True) 
    self.create_user(username, email, password, **kwargs)
  
  
  
# AbstractBaseUser: Django가 기본 제공하는 User모델을 대체하기 위해 사용되는 추상 클래스
# PermissionsMixin : User 모델에 대한 권한 부여하기 위한 클래스 

# 커스텀 유저 모델 
class CustomUser(AbstractBaseUser, PermissionsMixin):
  objects = CustomUserManager() #커스텀유저가, 커스텀유저매니저를 사용하겠다. 
  
  USERNAME_FIELD = 'username'   #인증 시, username 필드로 유저를 식별하겠다. 
  
  username = models.CharField(unique = True, max_length=20) 
  created_at = models.DateTimeField(auto_now_add=True) 
  updated_at = models.DateTimeField(auto_now=True)
  
  
  @property #is_staff를 속성처럼 사용
  def is_staff(self):
    return self.is_superuser  #
  
  
  
# 프로필 모델
class Profile(models.Model):
  #프로필:유저 = 일대일 관계
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile", null=True)
  nickname = models.CharField(max_length=20, null=True) 
  image = models.ImageField(upload_to='profile/', null=True)
  
  class Meta:
     db_table='profile'
  
  def __str__(self):
    return self.nickname  
  