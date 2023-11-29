from django import forms
from .models import Socios


class FormSocios(forms.ModelForm):
    class Meta:
        model = Socios
        fields = '__all__'

        ESTADO_CHOICES = [
            ('Vigente', 'VIGENTE'),
            ('Suspendido', 'SUSPENDIDO'),
            ('Retirado', 'RETIRADO'),
        ]
        SEXO_CHOICES = [
            ('Hombre', 'HOMBRE'),
            ('Mujer', 'MUJER'),
            ('Otro', 'OTRO'),
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaIncorporacion': forms.DateInput(attrs={'type': 'date'}),
            'añoNacimiento': forms.DateInput(attrs={'type': 'date'}),
            'telefono': forms.TextInput,
            'correo': forms.EmailInput,
            'sexo': forms.Select(choices=SEXO_CHOICES ),
            'estado': forms.Select(choices=ESTADO_CHOICES ),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }


    def clean_nombre(self, *args, **kwargs): 
        inputnombre = self.cleaned_data.get('nombre')
        if inputnombre and len(inputnombre) > 80:
            raise forms.ValidationError("El largo máximo es de 80 caracteres.")
        return inputnombre

    def clean(self):
        cleaned_data = super().clean()
        inputEmail = cleaned_data.get('correo')
        if inputEmail and '@' not in inputEmail:
            raise forms.ValidationError("El correo debe tener un @")
        return cleaned_data
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        telefono = ''.join(e for e in str(telefono) if e.isalnum())
        if len(telefono) !=9 or not telefono.isdigit():
            raise forms.ValidationError("El numero debe contener 9 digitos")
        return telefono
    
