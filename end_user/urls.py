from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("auth/api/v1/login/", views.LoginAPIView.as_view(), name="login"),
    path('auth/api/v1/refresh', views.RefreshAPIView.as_view()),
    path('auth/api/v1/user', views.UserAPIView.as_view()),
    path('auth/api/v1/list', views.GetAllUser.as_view()),
    path("auth/api/v1/logout/", views.LogoutView.as_view(), name="logout"),
]
