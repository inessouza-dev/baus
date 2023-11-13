from django.urls import path
from . import views

urlpatterns = [
    path('cadastro-admin/', views.cadastro_admin, name='cadastro-admin'),
    path('login-admin/', views.login_admin, name='login-admin'),
    path('access-admin/', views.access_admin, name='access-admin')
]