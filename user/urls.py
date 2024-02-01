from django.urls import path
from user.views import UserSignupView, LoginView

app_name = 'user'

urlpatterns = [
    path('register/',UserSignupView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
]
