from django.shortcuts import render, redirect, get_object_or_404 
from .models import Blog, Comment  # 모델 사용 

# Create your views here.

#urls.py에서 'home' 호출하면 views.py의 'home'함수가 실행됨
def home(request):
  blogs = Blog.objects.all()  #blog 테이블에 객체들을 all()이라는 메소드로 전부 가져오기 
  return render(request, 'home.html', {'blogs':blogs}) 
  #request(요청)이 들어오면 'home.html' 주소를 반환
  #가지고 온 blogs를 {'key':value} 형태로 보내주기 
  
def new(request):
  return render(request, 'new.html')  

# 글 작성 함수 
def post(request):
  new_blog = Blog() #new_blog라는 이름의 블로그 객체 새로 생성
  #id는 자동으로 생김
  new_blog.title = request.POST.get('title')  #
  new_blog.author = request.user 
  new_blog.content = request.POST.get('content') 
  new_blog.image = request.FILES.get('image') #파일 업로드는 request.FILES로 수신
  
  new_blog.save() #db에 새로 객체 저장
  
  return redirect('detail', new_blog.id) #새 글 작성 후 디테일 페이지로 이동 



# 글 세부 페이지 - id도 함께 받아와야 함 
def detail(request, blog_id):
  blog = get_object_or_404(Blog, pk= blog_id) #특정 id의 블로그 객체를 blog로 받기
  comments = Comment.objects.filter(blog=blog)
  return render(request, 'detail.html', {'blog': blog,'comments': comments,}) 




# 수정 페이지로 이동 
def edit (request, blog_id):
  edit_blog = get_object_or_404(Blog, pk = blog_id)
  
  if request.user != edit_blog.author:
        return redirect('home')

    
  return render(request, 'edit.html', {'edit_blog': edit_blog})



# 글 수정 작업
def update(request, blog_id):
  old_blog = get_object_or_404(Blog, pk = blog_id) #수정할 블로그 객체 가져오기
  
  #수정할 블로그 객체에 새 값 주기 
  old_blog.title = request.POST.get("title")  
  old_blog.content = request.POST.get("content")
  old_blog.image = request.FILES.get("image")
  old_blog.save() #수정한 블로그 db에 저장 
  return redirect('detail', old_blog.id) #상세 페이지로 이동 -> 수정된 내용 확인! 



# 글 삭제
def delete(request, blog_id):
  delete_blog = get_object_or_404(Blog, pk=blog_id)
  if request.user == delete_blog.author:
    delete_blog.delete()  #db에서 삭제 
    return redirect('home')  #삭제 후 메인홈으로 이동 
  return redirect("detail", delete_blog.id )


# 댓글 달기 창으로 연결
def new_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'new_comment.html', {'blog': blog})


# 댓글 생성 작업
def create_comment(request, blog_id):
    comment = Comment() # 댓글 객체 생성 
    comment.content = request.POST.get('content')
    
    comment.blog = get_object_or_404(Blog, pk=blog_id)
    comment.author = request.user 
    comment.save()
    return redirect('detail', blog_id)




