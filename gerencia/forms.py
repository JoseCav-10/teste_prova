from django import forms
from .models import Noticia, Categoria

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'texto': forms.Textarea(attrs={'class': 'form-control'}),  
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
            'image': forms.FileInput(attrs={'class': 'form-control'}), 
            'categoria': forms.Select(attrs={'class': 'form-control'}),

        }

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            "nome": forms.TextInput(attrs={"class":"form-control"})
        }
        
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        
        # Garantir que o nome seja único
        if Categoria.objects.filter(nome=nome).exists():
            raise forms.ValidationError("Já existe uma categoria com esse nome.")
        
        return nome



from django import forms
from .models import Categoria
from usuarios.models import UserBlog  # Importe o modelo de usuário personalizado

class NoticiaFilterForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        required=False,
        label='Título',
        widget=forms.TextInput(attrs={'placeholder': 'Digite o título','class': 'form-control'})
    )
    data_publicacao_inicio = forms.DateField(
        required=False,
        label='Data de Publicação (Início)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_publicacao_fim = forms.DateField(
        required=False,
        label='Data de Publicação (Fim)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label='Categoria',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
  
