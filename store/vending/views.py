from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):  # request(запрос) - ссылка на класс HttpRequest
    return HttpResponse('vending application page')  # (ответ)


def categories(request, cat_id):
    if request.GET:  # проверяем есть ли в запросе данные
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')
