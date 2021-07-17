from django.shortcuts import redirect, render, get_object_or_404, resolve_url #<!------이거 넣어야 get 함수 쓸 수 잇다 
# Create your views here.

from .models import Blog
from django.utils import timezone #이거 임포트 안해서 타임존 오류 생긴거엿넹
from .forms import BlogForm


def home(request):
     blog = Blog.objects #쿼리셋
     return render(request, 'home.html', {'blogs':blog}) # {} 이거 딕셔너리 형태! 딕셔너리 안에 blog 여러개(blogs)가 들어감 

def detail(request, blog_id):
        blog_detail = get_object_or_404(Blog, pk = blog_id) # 흠 이거 어렵군 
        return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
     form = BlogForm()
     return render(request, 'new.html', {'form':form}) #글 쓰는 창 띄우기

def create(request):
     form = BlogForm(request.POST, request.FILES) #유효성 검사 추가
     if form.is_valid():
          #new_blog = Blog() #모델(블로그) 클래스 상속인가? 
          #new_blog.title = request.POST['title']
          new_blog = form.save(commit=False) #임시 저장을 위한 커밋 펄스
          new_blog.body = request.POST['body']
          new_blog.pub_date = timezone.now()
          new_blog.save() #저장~
          return redirect('detail', new_blog.id) #이건 뭔 역할?,,, 왜 작동 안하지
     return redirect('home') #돌아가기!

def edit(request, blog_id):
     blog_detail = get_object_or_404(Blog, pk = blog_id)
     return render(request, 'edit.html', {'blog' : blog_detail})

def update(request, blog_id):
     blog_update = get_object_or_404(Blog, pk=blog_id)
     blog_update.title = request.POST['title']
     blog_update.body = request.POST['body']
     blog_update.save()
     return redirect('home')

def delete(request, blog_id):
     blog_delete = get_object_or_404(Blog, pk = blog_id)
     blog_delete.delete()
     return redirect('home')