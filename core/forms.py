from django.forms import ModelForm

from .models import URL

class URLForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['long_url'].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = URL
        fields = ('long_url',)
