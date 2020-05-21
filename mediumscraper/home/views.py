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
        print(request.POST['urlink'])

        if form.is_valid():
            res = req.get(form.cleaned_data['urlink']) 
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            content = ''
            if soup.find('article'):
                for i in soup.select('article'):
                    content += i.getText()
            else:
                print("This is not a medium article link..!")
                return render(request, 'home/index.html', {'form': form, 
                'text':"We could not find an article in this page. Please make sure this is a medium article link."})
            form = NameForm()
            val = content
        
        else:
            return render(request, 'home/index.html', {'form': form, 
                'text':"We could not find an article in this page. Please make sure this is a medium article link."})
    else:
        form = NameForm()
        val = "Please Enter a link"

    return render(request, 'home/index.html', {'form': form, 'text':val})
