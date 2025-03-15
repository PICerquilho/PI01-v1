from django.shortcuts import render,redirect
from .forms import AlunoForm
from .models import Aluno
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')

def cadastro(request):
    return render(request,'cadastro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a tela de login após logout

@permission_required('Sistema_Alunos.add_aluno', raise_exception=True)
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlunoForm()
    return render(request, 'cadastro.html', {'form': form})


def buscar_aluno(request):
    query = request.GET.get('q', '').strip()
    if query:
        alunos = Aluno.objects.filter(
            nome_social__icontains=query) | Aluno.objects.filter(
            nome__icontains=query) | Aluno.objects.filter(
            id_aluno__icontains=query) | Aluno.objects.filter(
            serie__icontains=query) | Aluno.objects.filter(
            periodo__icontains=query)
    else:
        alunos = Aluno.objects.all()

    resultado = [
        {
            'id_aluno': aluno.id_aluno,
            'nome': aluno.nome,
            'nome_social': aluno.nome_social,
            'serie': aluno.serie,
            'periodo': aluno.periodo,
            'foto': aluno.foto.url if aluno.foto else ''
        }
        for aluno in alunos
    ]
    return JsonResponse(resultado, safe=False)

def logout_view(request):
    messages.warning(request, "Sua sessão expirou por inatividade.")
    logout(request)
    return redirect('login')