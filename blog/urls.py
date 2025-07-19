from django.urls import path
from . import views


#a list that lists all the urls that we will make point to html pages/views
urlpatterns=[
    #index or homepage
    path('', views.post_list, name='post_list'),
    #post detail page
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #post create page
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
