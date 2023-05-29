from django.shortcuts import render, redirect

from .forms import URLForm
from .models import URL
from .models import Hits

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return render(request, 'index.html', {'form' : form, 'result' : instance.short_url})
        return render(request, 'index.html', {'form' : form, 'errors' : form.errors})
    return render(request, 'index.html', {'form' : URLForm()})

def redirect_view(request, short_url):
    try:
        destination = URL.objects.get(short_url=short_url)
        Hits.objects.create(url=destination)
        return redirect(destination.long_url)
    except URL.DoesNotExist as e:
        return redirect('/')