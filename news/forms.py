from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'heading',
            'category',
            'txt',
            'author',
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get('heading')
        txt = cleaned_data.get('txt')
        if heading == txt:
            raise ValidationError(
                {'heading': 'Описание не может быть идентично названию'}
            )
        return cleaned_data


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'heading',
            'category',
            'txt',
            'author',
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get('heading')
        txt = cleaned_data.get('txt')
        if heading == txt:
            raise ValidationError(
                {'heading': 'Описание не может быть идентично названию'}
            )
        return cleaned_data
