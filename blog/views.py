from time import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # posts: queryset name
    return render(request, 'blog/post_list.html', {'posts': posts})
    # render 함수를 호출하여 blog/post_list.html 템플릿을 보여줌
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})