from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  

# UserCreationForm
# AuthenticationForm


# 회원 가입 폼 -> 회원가입 시 유효성 검사
class CustomUserSignupForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['username']
    

# 로그인 (인증) 폼 -> 로그인 시 유효성 검사
class CustomUserSigninForm(AuthenticationForm):
  class Meta(UserCreationForm.Meta):
    models = CustomUser
    fields = ['username'] 