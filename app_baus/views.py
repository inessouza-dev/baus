from django.shortcuts import render, redirect
from .models import Voluntarios
from django.urls import path
from app_baus import views
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST' and request.POST:
        novo_voluntario = Voluntarios()
        novo_voluntario.nome = request.POST.get('nome')
        novo_voluntario.telefone = request.POST.get('telefone')
        novo_voluntario.email = request.POST.get('email')
        novo_voluntario.mensagem = request.POST.get('mensagem')
        novo_voluntario.save()
        return render(request, 'home.html', {'status': "Cadastro realizado com sucesso."})
    return render(request, 'home.html')

def cadastro_admin(request):
    if request.method == "GET":
        return render(request, 'admin/cadastro-admin.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user: 
            return HttpResponse('Usuário já existe.')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        return HttpResponse('Usuário cadastrado com sucesso!')

def login_admin(request):
    if request.method == "GET":
        return render(request, 'admin/login-admin.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('access-admin')
        else: 
            return HttpResponse('Email ou senha inválidos.')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def voluntarios(request):
    novo_voluntario = Voluntarios()
    novo_voluntario.nome = request.POST.get('nome')
    novo_voluntario.telefone = request.POST.get('telefone')
    novo_voluntario.email = request.POST.get('email')
    novo_voluntario.mensagem = request.POST.get('mensagem')
    novo_voluntario.save()

    voluntarios = {
        'voluntarios': Voluntarios.objects.all()
    }
    return render(request, 'home.html', voluntarios)

@login_required(login_url="/auth/login-admin/")
def access_admin(request):
    voluntarios = Voluntarios.objects.all()
    return render(request, 'admin/access-admin.html', {'voluntarios': voluntarios})