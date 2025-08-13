from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review', 'image']  # ← Добавили image
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название фильма',
            'description': 'Описание',
            'review': 'Ваш отзыв',
            'image': 'Постер фильма',
        }