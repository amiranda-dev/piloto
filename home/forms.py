# forms.py
from django import forms


from django import forms

class ContatoForm(forms.Form):
    # Definição das categorias para o campo de Assunto conforme o exercício
    CATEGORIAS = [
        ('suporte', 'Suporte técnico'),
        ('comercial', 'Comercial'),
        ('reclamacao', 'Reclamação'),
        ('parceria', 'Parceria'),
        ('financeiro', 'Financeiro'),
    ]

    nome = forms.CharField(
        max_length=100, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )

    # Novo campo: Telefone com o placeholder solicitado
    telefone = forms.CharField(
        label='Telefone / WhatsApp',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': '(99) 99999-9999'
        })
    )

    # Novo campo: Assunto usando o atributo choices
    assunto = forms.ChoiceField(
        choices=CATEGORIAS,
        label='Assunto do contato',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Escreva sua mensagem', 
            'rows': 4
        })
    )

# forms.py
class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100, 
        label='Nome do Produto:',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Digite o nome do produto'
        })
    )
    preco = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        label='Preço:',
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Digite o preço do produto'
        })
    )
