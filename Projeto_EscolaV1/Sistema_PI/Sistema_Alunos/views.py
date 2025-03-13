from django.shortcuts import render,redirect
from .forms import AlunoForm
from .models import Aluno
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def cadastro(request):
    return render(request,'cadastro.html')




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