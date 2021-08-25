from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('add',views.add),
    #path('test',views.test,name='link'),
    path('p=<int:id_>',views.page),
    path('<int:pk>',views.RecordView.as_view(),name='one'),
    path('about',views.about)
]
