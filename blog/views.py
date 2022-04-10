from django.shortcuts import render

# 一覧表示
def index(request):
    return render(request, 'blog/index.html')