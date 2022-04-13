from django.shortcuts import render
import datetime as dt

# 一覧表示
def index(request):
    # データを渡す
    context = {
        'title' :'django',
        'text' :'テストです。',
        'post_date' : dt.datetime(2022,12,1,8,56),
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