from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('id', 'Surname',  'Name', 'Mo_No', 'Std', 'Percentage', 'file')
        # widgets = {
        #     'Surname': forms.TextInput(attrs={'placeholder': 'Surname'}),
        #     'Name': forms.TextInput(attrs={'placeholder': 'Name'}),
        #     'Std': forms.TextInput(attrs={'placeholder': 'Std'}),
        #     'Percentage': forms.TextInput(attrs={'placeholder': 'Std'}),
        #     'file': forms.TextInput(attrs={'placeholder': 'File'})
        # }
