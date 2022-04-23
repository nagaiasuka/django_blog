from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('store',views.store,name='store'),
    path('<int:id>',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('comment/<int:id>',views.comment,name='comment'),
]
