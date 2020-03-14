from django.urls import path

from accounts.views import UserDetailView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<pk>/', UserDetailView.as_view(), name='detail'),

]

app_name = 'accounts'
