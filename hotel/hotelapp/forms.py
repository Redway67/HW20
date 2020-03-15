from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение')
