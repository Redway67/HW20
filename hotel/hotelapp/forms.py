from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение')


class BookingForm(forms.Form):
    who = forms.CharField(label='Фамилия')
    room = forms.ChoiceField(label='Номер')
    data_in = forms.DateField(label='Заезд')
    data_out = forms.DateField(label='Выезд')
    is_breakfast = forms.ChoiceField(label='Завтрак')
