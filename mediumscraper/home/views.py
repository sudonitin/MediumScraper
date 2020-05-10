from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import NameForm

import requests as req
import bs4
import warnings
warnings.simplefilter('ignore') 

def get_link(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            val = form.cleaned_data['urlink']
            res = req.get(val)
            soup = bs4.BeautifulSoup(res.text)

            if not soup.find('article'):
                return render(request, 'home/index.html', {'form': form, 
                'text':"We could not find an article in this page. Please make sure this is a medium article link."})

            content = ''
            for i in soup.find('article'):
                content += i.getText()
            val = "'" + content + "'"
            form = NameForm()

    else:
        form = NameForm()
        val = "'Please Enter a link'"

    return render(request, 'home/index.html', {'form': form, 'text':val})
