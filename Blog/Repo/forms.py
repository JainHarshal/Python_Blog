from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","author","description","code"]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'code':forms.Textarea(attrs={'class':'form-control'})
        }
