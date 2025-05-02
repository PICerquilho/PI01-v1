from django.db import models

class Aluno(models.Model):
    # Definir opções predefinidas
    SERIES_CHOICES = [
        ('1ª Ano', '1ª Ano'),
        ('2ª Ano', '2ª Ano'),
        ('3ª Ano', '3ª Ano'),
        ('4ª Ano', '4ª Ano'),
        ('5ª Ano', '5ª Ano'),
        ('6ª Ano', '6ª Ano'),
        ('7ª Ano', '7ª Ano'),
        ('8ª Ano', '8ª Ano'),
        ('9ª Ano', '9ª Ano'),
    ]
    
    TURMA_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    PERIODO_CHOICES = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
    ]

    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    id_aluno = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    rg = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    contato = models.CharField(max_length=15, blank=True, null=True)
    contato_emergencial = models.CharField(max_length=15, blank=True, null=True)
    responsavel = models.CharField(max_length=100, blank=True, null=True)
    

    # Agora os campos abaixo têm valores pré-definidos
    serie = models.CharField(max_length=10, choices=SERIES_CHOICES)
    turma = models.CharField(max_length=1, choices=TURMA_CHOICES)
    periodo = models.CharField(max_length=10, choices=PERIODO_CHOICES)

    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.serie} {self.turma} ({self.periodo})"
