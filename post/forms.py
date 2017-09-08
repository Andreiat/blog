from blog.post.models import CommentPost
from django.forms import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('text',)