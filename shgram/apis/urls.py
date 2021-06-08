from django.urls import path

from apis.views import (
    UserCreateView, UserLoginView, UserLogoutView, ContentCreateView, RelationCreateView, RelationDeleteView,
    UserGetView
)
urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/login', UserLoginView.as_view(), name='user_login'),
    path('users/logout', UserLogoutView.as_view(), name='user_logout'),
    path('users/contentCreate', ContentCreateView.as_view(), name='content_create'),
    path('users/relations/create',
         RelationCreateView.as_view(), name='relation_create'),
    path('users/relations/delete',
         RelationDeleteView.as_view(), name='relation_delete'),
    path('users/get', UserGetView.as_view(), name='users_get_info'),

]
