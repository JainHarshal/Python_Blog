from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('articles',views.Postview.as_view(),name="articles"),
    path('add',views.Addpost.as_view(),name="Add_Post"),
    path('details/<int:pk>',views.Detailpost.as_view(),name="details"),
    path('delete/<int:pk>',views.Deletepost.as_view(),name='delete'),
    path('edit/<int:pk>',views.Editview.as_view(),name="edit"),
    
]


