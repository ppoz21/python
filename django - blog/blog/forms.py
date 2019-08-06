from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    imię = forms.CharField(max_length=25)
    e_mail = forms.EmailField()
    do = forms.EmailField()
    komentarz = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()
