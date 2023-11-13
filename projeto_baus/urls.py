from django.urls import path, include
from django.contrib import admin
from app_baus import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('auth/', include('app_baus.urls'))
]
