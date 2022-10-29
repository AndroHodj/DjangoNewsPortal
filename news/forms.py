from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Category


class NewsForm(forms.ModelForm):
    article_or_news = forms.ChoiceField(label='Type', choices=Post.CATEGORIES)

    category = forms.ModelMultipleChoiceField(
        label='Category',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Post
        fields = [
            'heading',
            'txt',
            'author',
            'article_or_news',
            'category',
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
