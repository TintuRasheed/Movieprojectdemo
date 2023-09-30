from .models import Movie
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['Name','Desc','year','Img']
        