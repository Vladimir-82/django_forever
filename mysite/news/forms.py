from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


# форма не связанная с моделью (не желательна к использованию)
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название:')
#     content = forms.CharField(label='Текст:', required=False)   # required=False - делает поле не обязательным
#     is_published = forms.BooleanField(label='Опубликовано?', initial=True)  # делает чекбокс по умолчанию отмеченным
#     category = forms.ModelChoiceField(empty_label="Выберите категорию", label='Категория:', queryset=Category.objects.all())    # empty_label="Выберите категорию" изменяет заглавие выпадающего меню
