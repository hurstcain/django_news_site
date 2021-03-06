from django import forms
from news.models import Category, News


'''class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    content = forms.CharField(required=False, label='Содержание', widget=forms.Textarea(
        attrs={'class': 'form-control'}
    ))
    photo = forms.ImageField(required=False, label='Фотография')
    is_published = forms.BooleanField(initial=True, label='Опубликовано')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, label='Категория', widget=forms.Select(
        attrs={'class': 'form-select'}
    ))'''


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
