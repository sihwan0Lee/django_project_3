from django.urls import path

from apis.views import UserCreateView, UserLoginView

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/login', UserLoginView.as_view(), name='user_login')


]
