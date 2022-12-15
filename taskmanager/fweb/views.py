from django.shortcuts import render, redirect
from .models import FizProperties
from .forms import FizPropertiesForm


def indexF(request):
    prop = FizProperties.objects.order_by('id')
    return render(request, 'fweb/index.html', {'title': 'Main page of web-site', 'prop': prop})


def aboutF(request):
    return render(request, 'fweb/aboutF.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = FizPropertiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeF')
        else:
            error = 'form isnt valid'

    form = FizPropertiesForm()
    context = {
        'form': form
    }
    return render(request, 'fweb/create.html', context)