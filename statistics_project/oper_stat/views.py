import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .crud_func import read_report_oper, read_report_oper_with_date
from .forms import QueryStatForm


def home(request: HttpRequest):
    """
    Представление - Главная страница.
    :param request: HttpRequest - запрос пользователя.
    :return: Страница приветствия.
    """
    return render(request, 'home.html')


def report_oper(request: HttpRequest, pk: str | None = None):
    """
    Предоставляет статистику по оператору в формате json.
    :param request: HttpRequest - запрос пользователя.
    :param pk: Имя оператора
    :return: Данные в формате json
    """
    if request.method == 'GET':
        report = read_report_oper(pk)
    else:
        report = None
    return HttpResponse(json.dumps(report))


def report_all(request: HttpRequest):
    """
    Предоставляет статистику по всем операторам в формате json.
    :param request: HttpRequest - запрос пользователя.
    :return: Данные в формате json
    """
    if request.method == 'GET':
        report = read_report_oper()
    else:
        report = None
    return HttpResponse(json.dumps(report))


def report_form(request: HttpRequest):
    """
    Предоставляет статистику по запросу из формы в формате json.
    :param request: HttpRequest - запрос пользователя.
    :return: Данные в формате json
    """
    if request.method == 'POST':
        form = QueryStatForm(request.POST, request.FILES)
        if form.is_valid():
            from_date = form.data.get('from_date')
            to_date = form.data.get('to_date')
            report = read_report_oper_with_date(from_date, to_date, oper=form.data.get('operator'))
            return HttpResponse(json.dumps(report))
    else:
        form = QueryStatForm()
    return render(request, 'oper_stat/request_statistic_oper.html',
                  context={'form': form})
