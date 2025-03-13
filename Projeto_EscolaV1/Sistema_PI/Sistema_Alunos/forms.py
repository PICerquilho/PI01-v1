from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Para exibir um seletor de data

    class Meta:
        model = Aluno
        fields = '__all__'  # Usa todos os campos do modelo
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_social': forms.TextInput(attrs={'class': 'form-control'}),
            'id_aluno': forms.TextInput(attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_emergencial': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'turma': forms.TextInput(attrs={'class': 'form-control'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'periodo': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }