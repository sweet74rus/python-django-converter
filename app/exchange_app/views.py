from pydoc_data.topics import topics
from django.shortcuts import render
import requests

def exchange(request):
    response = requests.get(url="https://api.exchangerate-api.com/v4/latest/USD").json()
    curr = response.get('rates')

    if request.method == 'GET':
         
        context = {
             'curr' : curr,
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)

    if request.method == 'POST':

        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')
    
        converted_amount = round((curr[to_curr] / curr[from_curr]) * float(from_amount), 2)

        context = {
            'from_amount' : from_amount,
            'from_curr' : from_curr,
            'to_curr' : to_curr,
            'curr' : curr,
            'converted_amount' : converted_amount,
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)
