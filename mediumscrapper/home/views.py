from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import NameForm

import requests as req
import bs4
import warnings
warnings.simplefilter('ignore') 

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
            val = form.cleaned_data['urlink']
            print(str(val))
            res = req.get(val)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            content = ''
            for i in soup.select('article'):
                content += i.getText()

            val = content
            form = NameForm()
            # return redirect('home:home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        val = 'first time'
        print(str(val))

    return render(request, 'home/index.html', {'form': form, 'text':val})
