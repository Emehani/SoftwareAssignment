from django import forms
from .models import Bloog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Bloog
        fields = ["name", "description", "tags"]