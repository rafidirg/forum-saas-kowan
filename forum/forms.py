from forum.models import Post, Comment
from django import forms
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'slug', 'course']

    title = forms.CharField(
        label='Title',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'required': 'True',
                'placeholder': 'Enter post title'
            }))

    content = forms.CharField(widget=TinyMCE())


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'post', 'course']

    content = forms.CharField(label='Message', widget=TinyMCE())
