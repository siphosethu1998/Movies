from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie # the table
        fields = '__all__' # all the columns for your table
