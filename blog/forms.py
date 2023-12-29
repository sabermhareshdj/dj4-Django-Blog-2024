from django import forms
from .models import Post ,Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget 
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField



class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        #fields = '__all__'
        exclude = ('author',)
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

