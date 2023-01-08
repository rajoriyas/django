from django import forms
from blogging_world_app.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'textinputclass form-control'}),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcontent form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass form-control'}),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcontent form-control'})
        }
