from django.shortcuts import render,get_object_or_404,redirect
import datetime as dt
from blog.models import Post,Comment
from .forms import CommentCreateForm

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
    # データの受け取り
    post = Post(
        title = request.POST.get('title'),
        text = request.POST.get('text'),
        user = request.user,
    )
    post.save()
    # データの保存
    # リダイレクト
    return redirect(index)

# 詳細画面
def show(request,id):
      # データの取り出し
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(target=id)
    # データを渡す
    context = {
        'post': post,
        'comments':comments
    }
    
    return render(request, 'blog/show.html',context)

# 編集更新画面
def edit(request,id):
       # データの取り出し
    post = get_object_or_404(Post, pk=id)
    # データを渡す
    context = {
        'post': post,
    }
    return render(request, 'blog/edit.html',context)

# 更新処理
def update(request,id):
    post = Post(
        pk = id,
        title = request.POST.get('title'),
        text = request.POST.get('text'),
    )
    post.save(
        update_fields=[
            'title',
            'text',
            'updated_at',
        ]
    )
    return redirect(index)


# 削除
def delete(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect(index)

#コメント
def comment(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == 'POST':
        commentCreateForm= CommentCreateForm(request.POST)
        if commentCreateForm.is_valid():
            comment = commentCreateForm.save(commit=False) 
            comment.user=request.user
            comment.target=post
            comment.save()
            return redirect(show,id)
    else:
        commentCreateForm = CommentCreateForm()
    
    context = {
        'post' : post,
        'form' : commentCreateForm,
    }
    
    return render(request, 'blog/comment.html',context)