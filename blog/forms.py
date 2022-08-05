from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: # what model should be used to create this form? (model = Post)
        model = Post
        fields = ('title', 'text',)