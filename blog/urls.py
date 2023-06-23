from django.urls import path
from . import views  

urlpatterns = [
    # MAIN 
    path('', views.home, name='home'),  #blog앱 views.py     # 127.0.0.1:8000
    
    # CREATE 
    path('blog/new/', views.new, name='new'),  #홈에서 글 작성 페이지로 이동 
    path('blog/post/', views.post, name='post'), 
    
    # READ 
    path('blog/<int:blog_id>/', views.detail, name = 'detail'),
    
    # EDIT
    path('blog/edit/<int:blog_id>/', views.edit, name='edit'), #글 수정 페이지 
    path('blog/update/<int:blog_id>', views.update, name='update'), #글 수정하는 작업 
    
    #DELETE 
    path('blog/delete/<int:blog_id>', views.delete, name='delete'), #글 삭제 

    #COMMENT
    path('blog/<int:blog_id>/new_comment/', views.new_comment, name='new_comment'),
    path('blog/<int:blog_id>/create_comment/', views.create_comment, name='create_comment')
    # #LIKE 
    ]
