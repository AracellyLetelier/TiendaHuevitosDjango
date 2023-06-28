from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields="__all__"
        widgets={
                'descripcion':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar una Descipcion del produto',
                        'class':'form-control'
                        }
                    ),
                'precio':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar precio',
                        'class':'form-control',
                        'type':'number'
                        }
                    ),
                'Stock':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar Stock',
                        'class':'form-control',
                        'type':'number'
                        }
                    ),
                'Categoria':forms.Select(
                    attrs={                   
                        'class':'form-control'
                        }
                    )              
                }