from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import NameForm

def get_link(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            text = form.cleaned_data['urlink']
            print(str(text))
            form = NameForm()
            # return redirect('home:home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        text = 'first time'
        print(str(text))

    return render(request, 'home/index.html', {'form': form, 'text':text})
