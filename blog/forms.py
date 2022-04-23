from django import forms
from.models import Comment

class CommentCreateForm(forms.ModelForm):
    class Meta:
        moedl = Comment
        fields = ("text",)
