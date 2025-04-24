from django.urls import path, include # type: ignore
from . import views

urlpatterns = [
    path('',views.index),
    path('open_signin', views.open_signin, name='open_signin'),
    path('open_signup', views.open_signup, name='open_signup'),
    path('signup', views.signup, name='signup'),
]
