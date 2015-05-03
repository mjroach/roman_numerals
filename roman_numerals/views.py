from django.http import HttpResponse
import datetime

from django.shortcuts import render

from forms import IntergerForm

def home(request):
    context = {}


    if request.POST:
        #we have the page being submitted, time to validate it
        form = IntergerForm(request.POST)

        if form.is_valid():
            ##form is valid
            context['result'] = 5
            import ipdb; ipdb.set_trace()


    form = IntergerForm() #base empty form

    context['form'] =  form
    return render(request, 'home.html', context)

