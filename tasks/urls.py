from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('update/<int:pk>',views.update_task,name='update'),
    path('delete/<int:pk>',views.delete_task,name='delete'),
]