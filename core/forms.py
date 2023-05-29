from django.forms import ModelForm

from .models import URL

class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ('long_url',)
