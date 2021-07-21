from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy



class Postview(ListView):
    model=Post
    template_name="articles.html"

class Addpost(CreateView):
    model=Post
    form_class=PostForm
    template_name="add_post.html"

class Detailpost(DetailView):
    model=Post
    template_name='details.html'

class Deletepost(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('articles')

class Editview(UpdateView):
    model=Post
    form_class=PostForm
    template_name="edit_post.html"

def home(request):
    return render(request,'about_me.html')



