from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('add',views.add),
    #path('test',views.test,name='link'),
    path('p=<int:id_>',views.page),
    path('<int:pk>',views.RecordView.as_view(),name='one'),
    path('<int:pk>/edit',views.RecordUpdate.as_view(),name='edit'),
    path('about',views.about),
    path('sign',views.signup),
    path('test',views.test),
    path('login',views.LogIn,name='login'),
    path('logout',views.LogOut,name='logout'),
    path('comment/<int:pk>',views.comment,name='comment'),
    path('like/<int:pk>', views.like, name='like')
]
