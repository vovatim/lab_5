from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return HttpResponse("Hello, welcom in our Bukmekerskuy kontoru 'Sorvi Kush'.")

class ExampleView(View):
    def get(self, reguest):
        return render(reguest, 'example.html', {'my_variable':'Здесь объявляется переменная', 'list': [1,2,3]})

class OrdersView(View):
    def get(self, request):
        data = {
            'orders':[
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3},
            ]
        }
        return render (request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {
            'orders': [
                {'id':int(id)}
            ]
        }
        print(data)
        return render(request, 'orders.html', data)