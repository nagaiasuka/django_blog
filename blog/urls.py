from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('store',views.store,name='store'),
    path('<int:id>',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update',views.update,name='update'),
    path('comment',views.comment,name='comment'),
    # path('<int:id>/delete',views.destoroy,name='delete')
]
