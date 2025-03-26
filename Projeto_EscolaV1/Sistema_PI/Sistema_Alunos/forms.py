from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Aluno
        fields = '__all__'  # Isto garante que todos os campos, incluindo o 'endereco', sejam exibidos no formulário.
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
            'serie': forms.Select(attrs={'class': 'form-control'}),
            'turma': forms.Select(attrs={'class': 'form-control'}),
            'periodo': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control'}),
        }
