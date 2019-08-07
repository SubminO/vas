from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy, include
from auth_user import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='auth_user/login.html'),
    #      name='login'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
]
