from django.shortcuts import render

import requests
from django.http import  HttpResponse
from django import forms
from django.views.generic import TemplateView
from .forms import homeform


def home(request):
    if request.method == 'POST':

        form = homeform(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            field = text['name']

            print(field)
            if str(field) == 'france':
                print('true')


            country = field

    else:

        form = homeform()
        country = 'Algeria'
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country": country}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "36b864062emshac7e191eb5087e6p169e6bjsn24c86f3408c1"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data = response['response']
    print(data)
    d = data[0]
    context = {
        'all': d['cases']['total'],
        'recovered': d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'serious': d['cases']['critical'],
        'active': d['cases']['active'],
        'deaths_new': d['deaths']['new'],
        'form': form,
        'country':d['country']

    }

    return render(request, 'index.html', context)