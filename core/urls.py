from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('delete', delete, name="delete"),
    path('search', search, name="search"),
    path('profile', myProfile, name="myProfile"),
    path('profile/<int:id>', profilepage, name="profilepage"),
    path('update_post/<int:id>', update_post, name="update_post"),
    path('friend/<int:id>/<str:username>', friends, name="friends"),
]
