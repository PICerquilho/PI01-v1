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
    query = request.GET.get('q', '').strip()  # Pegando o parâmetro de busca

    if query:
        alunos = Aluno.objects.filter(
            Q(nome__icontains=query) |  # Buscando pelo nome
            Q(nome_social__icontains=query) |  # Buscando pelo nome social
            Q(id_aluno__icontains=query) |  # Buscando pelo RA (id_aluno)
            Q(rg__icontains=query) |  # Buscando pelo RG
            Q(serie__icontains=query) |  # Buscando pela série
            Q(periodo__icontains=query)  # Buscando pelo período
        )
    else:
        alunos = Aluno.objects.none()  # Caso a query esteja vazia, não retorna nenhum aluno

    resultados = []
    for aluno in alunos:
        resultados.append({
            'id': aluno.id,
            'nome': aluno.nome,
            'nome_social': aluno.nome_social,
            'id_aluno': aluno.id_aluno,
            'foto': aluno.foto.url if aluno.foto else '',
            'serie': aluno.serie,
            'periodo': aluno.periodo,
        })

    return JsonResponse(resultados, safe=False)