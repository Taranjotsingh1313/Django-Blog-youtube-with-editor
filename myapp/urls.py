from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login1,name='login'),
    path('signup/',views.signup,name='signup'),
    path('Blog',views.blog,name='blog'),
    path('post/<int:postid>',views.post,name='index'),
    path('logout/',views.logout1)
]
