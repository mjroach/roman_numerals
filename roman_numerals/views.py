from django.shortcuts import render

from roman import int_to_roman
from forms import IntergerForm


def home(request):
    context = {}

    if request.POST:
        # we have the page being submitted, time to validate it
        form = IntergerForm(request.POST)
        if form.is_valid():
            ##form is valid
            context['result'] = int_to_roman(form.cleaned_data['input'])

    else:
        form = IntergerForm()  # base empty form


    context['form'] = form
    return render(request, 'home.html', context)

