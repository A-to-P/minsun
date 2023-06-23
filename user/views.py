from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout #장고 제공 로그인, 로그아웃 사용
# 폼 사용 
from .forms import CustomUserSignupForm, CustomUserSigninForm

# 모델 사용 
from .models import CustomUser, Profile 


# Create your views here.

# 회원 가입
def signup(request):
  form = CustomUserSignupForm() #폼 생성 
  
  #착한 사용자 
  if request.method == "POST":
    form = CustomUserSignupForm(request.POST)  #사용자의 입력값만 유효한지 판단 

  
    if form.is_valid(): # 유효할 경우 
      user = form.save()  #폼 데이터를 db에 저장 
      login(request, user)  #장고 제공 login() 
      return redirect("home")  #회원가입 후 메인홈으로 이동 
  
  #나쁜 사용자   
  return render(request, "newSignup.html", {"form" : form}) 
  #회원가입 페이지로 이동 , 유효성 검사 하도록 객체도 함께 전달


  
# 로그인
def signin(request):
  form = CustomUserSigninForm() #폼 객체 생성 
  
  #착한 사용자
  if request.method == "POST":
    form = CustomUserSigninForm(request, request.POST) 
    
    if form.is_valid(): #유효하다면
      login(request, form.get_user()) #로그인 -> db에서 일치하는지만 확인! / db save() 필요 없음
      return redirect('home') #로그인 후 메인홈으로 이동
    
  #나쁜 사용자 
  return render(request, "newSignin.html", {"form" : form})
  

# 로그아웃
def signout(request):
  logout(request)
  return redirect("home") #유저 로그아웃 후 메인홈으로 이동

# 프로필 
def new_profile(request):
  # 로그인 하지 않았다면, 프로필을 누르더라도 계속 홈으로 이동 
  if request.user.is_anonymous:
    return redirect("home") 
  
  # 로그인 했다면 -> 해당 유저의 프로필 보여주기
  profile, created = Profile.objects.get_or_create(user=request.user) 
  
  # request.user : 현재 요청 보내는 유저
  # get_or_created(조건) 메서드 : 주어진 조건에 따라 객체를 가져오거나 존재하지 않으면 생성
  # user=request.user : user 필드가 request.user와 일치하는 프로필을 가져오거나 생성할 것을 지정
  # 반환 : 1. 가져온(생성된) 프로필 객체  2.객체가 새로 생성되었는지 여부를 나타내는 bool값 -> 이 값을 created에 지정
  
  # created == False : 이미 해당 유저의 프로필 객체가 존재해서 get했음(새로 생성X)
  # created == True : 해당 유저의 프로필 객체가 존재하지 않아서 새로 생성했음
  
  return render(request, "newProfile.html", {"profile":profile}) #가져온 프로필 객체를 전달, 프로필 페이지로 이동



# 프로필 생성 작업
def create_profile(request):
  profile, created = Profile.objects.get_or_create(user=request.user)
  
  if request.method == 'POST':
        profile.nickname = request.POST.get('nickname')
        profile.image = request.FILES.get('image')
        profile.save()
        return redirect('user:new_profile')

  return render(request, 'newProfile.html', {'profile': profile})
