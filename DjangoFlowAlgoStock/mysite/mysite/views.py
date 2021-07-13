from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Home")

def charts(request):

    return render(request, 'charts.html')

def uvolume(request):
    # context = {}
    # sticker = request.POST.get('sticker', None)
    # context['sticker'] = sticker
    # data_start = request.POST.get('data_start', None)
    # context['data_start'] = data_start
    # data_end = request.POST.get('data_end', None)
    # context['data_end'] = data_end
    import requests
    import json

    url = "https://twelve-data1.p.rapidapi.com/stocks"

    querystring = {"exchange": "NASDAQ", "format": "json"}

    headers = {
        'x-rapidapi-key': "9c714f9a9fmsh22461f0b6d7e572p1bb1b3jsn9e2c7d195b1c",
        'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = json.loads(response.text)

    return render(request, 'unusualvolume.html', response)