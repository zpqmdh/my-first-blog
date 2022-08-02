from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    # render 함수를 호출하여 blog/post_list.html 템플릿을 보여줌