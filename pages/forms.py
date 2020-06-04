from django import forms


class ModalLesson(forms.Form):
    child_name = forms.CharField(label='ФИО ребёнка', max_length=25,
                                 widget=forms.TextInput(attrs={'placeholder': 'Введите ФИО ребёнка'}))
    choices = (
        ('1-2 класс', '1-2 класс'),
        ('3-4 класс', '3-4 класс'),
        ('5-8 класс', '5-8 класс'),
    )
    age = forms.ChoiceField(label='Возрастная категория', choices=choices)
    parent_name = forms.CharField(label='Ваше ФИО', max_length=25,
                                  widget=forms.TextInput(attrs={'placeholder': 'Введите ваше ФИО'}))
    phone_number = forms.CharField(label='Ваш номер телефона', max_length=12,
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Введите ваш номер телефона', 'type': 'tel'}))

