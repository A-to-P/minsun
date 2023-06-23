# Myblog/blog/models.py 
from django.db import models
from user.models import CustomUser 

# Create your models here.

# 블로그 모델 
class Blog(models.Model):  #models.Model은 고정 형식
  #모델 클래스명은 단수형을 사용하는 게 좋음
  #id는 자동적으로 추가
  #models.Model을 상속받는 Class로 작성 
  title = models.CharField(max_length = 200)  #블로그 제목 
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)  
  content = models.TextField()  #작성할 내용 
  created_at = models.DateTimeField(auto_now_add=True) #실시간 날짜, 시간 출력
  #updated_at = models.DateTimeField(blank=True, null=True) #수정일
  image = models.ImageField(upload_to = 'blog/', null = True ) #이미지 저장될 위치 : media/blog/파일 
  

  # def update_date(self):  #나중에 수정할 때 사용하는 함수
  #   self.updated_at = timezone.now()  
  #   self.save() 
    #인스턴스의 updated_at 필드를 현재 시간으로 변경, 바뀐 정보 db엔 저장 
  
  #페이지에서 보여지는 객체의 정보 - title 
  def __str__ (self):
    return self.title 
  
  
  def summary(self):
    return self.content[:100]
  
  

# 댓글 모델
class Comment(models.Model):
  content = models.CharField(max_length= 100) #CharField:단일 라인 입력, 최대 길이 정의 필요
  created_at = models.DateTimeField(auto_now_add=True)  
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True) #on_detete 옵션 => CASCADE : ForeignKey가 삭제되면 이 data도 사라진다
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
  
  class Meta:
    db_table = 'comment'
  
  def __str__(self):
    return self.content + "|" + str(self.author) 
  
  
  