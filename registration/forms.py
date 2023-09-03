# para traer los atributos de forms en este caso los widget
from django import forms

""" UserCreationForm
 está diseñada específicamente para facilitar la creación de formularios de registro de usuarios. Proporciona campos para el nombre de usuario, la dirección de correo electrónico y la contraseña del usuario, y realiza automáticamente las validaciones necesarias y la lógica de creación de usuario en la base de datos cuando se envía el formulario.
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enlace'}),
        }


class EmailForms(forms.ModelForm):
    email = forms.EmailField(
        required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "El email ya está registrado, prueba con otro.")
        return email


"""
def clean_email(self):
    # Obtener el valor del campo "email" del formulario
    email = self.cleaned_data.get("email")

    # Verificar si el campo "email" ha sido modificado en el formulario
    if 'email' in self.changed_data:
        # Si el campo "email" ha sido modificado, verificar si ya existe en la base de datos
        if User.objects.filter(email=email).exists():
            # Si existe, levantar una excepción de validación
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")

    # Devolver el valor del campo "email" validado
    return email

"""
