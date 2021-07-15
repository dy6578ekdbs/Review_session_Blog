from django.shortcuts import render, get_object_or_404 #<!------이거 넣어야 get 함수 쓸 수 잇다 
# Create your views here.

from .models import Blog
 
def home(request):
     blog = Blog.objects #쿼리셋
     return render(request, 'home.html', {'blogs':blog}) # {} 이거 딕셔너리 형태! 딕셔너리 안에 blog 여러개(blogs)가 들어감 

def detail(request, blog_id):
        blog_detail = get_object_or_404(Blog, pk = blog_id)
        return render(request, 'detail.html', {'blog': blog_detail})