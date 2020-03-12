from django import forms
from .models import BookingOrder, Client, Room


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение')


class BookingForm(forms.ModelForm):
    who = forms.CharField(label='Гость',
                          widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию и имя', 'class': 'form-control'}))
    # Номер комнаты вводит Администратор
    # room = forms.ModelChoiceField(queryset=Room.objects.all())
    data_in = forms.DateField(label='Заезд')
    data_out = forms.DateField(label='Выезд')
    is_breakfast = forms.ChoiceField(label='Завтрак')

    class Meta:
        model = BookingOrder
        fields = '__all__'
        exclude = ('room',)
