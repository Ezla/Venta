#encoding utf-8
from django import forms

from .models import Producto

class CrearProductoForm(forms.ModelForm):
	#codigo = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control',}))
	#descripcion = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Codigo de barras'}))
	#p_unitario = forms.DecimalField(widget = forms.NumberInput(attrs={'class':'form-control',}))
	#p_mayoreo = forms.DecimalField(widget = forms.NumberInput(attrs={'class':'form-control',}))
	#inventario = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-control',}))
	#cantidad = forms.IntegerField(widget = forms.NumberInput(attrs={'class':'form-control',}))
	#minimo = forms.IntegerField(widget = forms.NumberInput(attrs={'class':'form-control'},))

	class Meta:
		model =Producto
		fields = '__all__'
		widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control',}),
            'descripcion': forms.TextInput(attrs={'class':'form-control',}),
            'punitario': forms.NumberInput(attrs={'class':'form-control',}),
            'pmayoreo': forms.NumberInput(attrs={'class':'form-control',}),
            'inventario': forms.CheckboxInput(attrs={'class':'form-control',}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control',}),
            'minimo': forms.NumberInput(attrs={'class':'form-control',}),
        }

	