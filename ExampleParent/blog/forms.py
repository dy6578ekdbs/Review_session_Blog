from django import forms
from django.db.models import fields
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta: #일종의 이름표 역할
        model = Blog
        fields = ['title', 'body'] #이게 뭐지???? 