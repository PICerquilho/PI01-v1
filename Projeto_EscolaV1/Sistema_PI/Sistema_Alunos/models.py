from django.db import models

class Aluno(models.Model):
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)  # Foto do aluno
    id_aluno = models.CharField(max_length=20, unique=True, blank=True, null=True)  # ID único para o aluno
    nome = models.CharField(max_length=100)  # Nome completo
    nome_social = models.CharField(max_length=100, blank=True, null=True)  # Nome social (opcional)
    rg = models.CharField(max_length=20, unique=True)  # RG (único)
    cpf = models.CharField(max_length=14, unique=True)  # CPF (único)
    data_nascimento = models.DateField()     # Data de nascimento
    contato = models.CharField(max_length=15, blank=True, null=True)  # Contato (telefone)
    contato_emergencial = models.CharField(max_length=15, blank=True, null=True)  # Contato de emergência
    responsavel = models.CharField(max_length=100, blank=True, null=True)  # Responsável
    turma = models.CharField(max_length=50)  # Turma/Série/Período (como texto)
    serie = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True, null=True)  # Observações sobre o aluno

    # Método para exibir o nome do aluno no painel admin
    def __str__(self):
        return self.nome