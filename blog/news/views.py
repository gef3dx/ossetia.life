from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

#Отображения всех постов
class PostView(ListView):
    model = Post
    context_object_name = "post"
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(posted=True).select_related('category')

#Отображение одного поста
class SinglePostView(DetailView):
    model = Post
    context_object_name = "singlepost"

