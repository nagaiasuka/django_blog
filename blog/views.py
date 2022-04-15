from django.shortcuts import render
import datetime as dt
from blog.models import Post

# 一覧表示
def index(request):
    # データの取り出し
    posts = Post.objects.all()
    # データを渡す
    context = {
        'posts': posts,
    }
    
    return render(request, 'blog/index.html',context)

# 新規投稿
def create(request):
    return render(request, 'blog/create.html')

# 登録処理
def store(request):
    pass

# 詳細画面
def show(request):
    return render(request, 'blog/show.html')

# 編集更新画面
def edit(request):
    return render(request, 'blog/edit.html')

# 更新処理
def update(request):
    pass

# 削除
def delete(request):
    pass

#コメント
def comment(request):
    return render(request, 'blog/comment.html')