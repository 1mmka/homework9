from django.shortcuts import render
import requests
from app.models import *

# Create your views here.
def input_data(request):
    return render(request,'index.html')

def get_data(request):
    if request.method == 'POST':
        request_data = request.POST
        url = 'https://jsonplaceholder.typicode.com/todos?_limit=%s' % request_data['amount']
        response = requests.get(url)
        data = response.json()
        '''после отправки данных через input в index.html
            беру эту цифру/число и пишу его в лимиты url-а фейк API
            заполняю временный список данными из title
            и вызываю методы класса'''


        temp_list = []
        for i in range(0,len(data),1):
            temp_list.append(data[i]['title'])
        
        todos_title = TodosTitle()
        todos_title.set_my_list(temp_list)

        return render(request,'data.html',{'todos_title':todos_title.get_my_list()})