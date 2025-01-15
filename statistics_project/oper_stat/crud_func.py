import logging
from datetime import datetime

from django.db import connection


def read_report_oper(oper: str = None, query_lst=None) -> dict:
    """
    Выполнить запросы статистики по списку query_lst
    :param oper: Оператор, по которому требуется статистика, если None, то по всем операторам
    :param query_lst: Список запросов, по умолчанию все запросы
    :return: Результаты всех запросов в формате dict
    """
    from .sql_query.sql_statistic import (
        count_success_call, avg_success_call_in_dey, avg_conversion_call_in_dey,
        avg_duration_success, avg_duration_not_success)

    if query_lst is None:
        query_lst = [
            (count_success_call, 'count_success_call'),
            (avg_success_call_in_dey, 'avg_success_call_in_dey'),
            (avg_conversion_call_in_dey, 'avg_conversion_call_in_dey'),
            (avg_duration_success, 'avg_duration_success'),
            (avg_duration_not_success, 'avg_duration_not_success')
        ]
    result: dict = {}
    try:
        with connection.cursor() as cursor:
            for query in query_lst:
                cursor.execute(query[0])
                rows = cursor.fetchall()
                print(rows)
                # Берем данные с учетом oper
                result[query[1]] = [x for x in rows if x[0] == oper or not oper]
    except Exception as er:
        msg = f'Ошибка выполнения запроса: {er.args}'
        print(msg)
        logging.error(msg)

    return result


def read_report_oper_with_date(from_date, to_date, oper: str = None, query_lst=None) -> dict:
    """
    Выполнить запросы статистики по списку query_lst с учетом периода расчета
    :param from_date: Дата начала периода
    :param to_date: Дата окончания периода
    :param oper: Оператор, по которому требуется статистика, если None, то по всем операторам
    :param query_lst: Список запросов, по умолчанию все запросы
    :return: Результаты всех запросов в формате dict
    """
    from .sql_query.sql_statistic_with_date import (
        count_success_call, avg_success_call_in_dey, avg_conversion_call_in_dey,
        avg_duration_success, avg_duration_not_success)

    if query_lst is None:
        query_lst = [
            (count_success_call, 'count_success_call'),
            (avg_success_call_in_dey, 'avg_success_call_in_dey'),
            (avg_conversion_call_in_dey, 'avg_conversion_call_in_dey'),
            (avg_duration_success, 'avg_duration_success'),
            (avg_duration_not_success, 'avg_duration_not_success')
        ]
    # По умолчанию даты начала и окончания периода расчета:
    if not from_date:
        from_date = datetime.now().date().replace(day=1)
    if not to_date:
        to_date = datetime.now().date()

    result: dict = {}
    try:
        with connection.cursor() as cursor:
            for query in query_lst:
                cursor.execute(query[0], (from_date, to_date))
                rows = cursor.fetchall()
                print(rows)
                # Берем данные с учетом oper
                result[query[1]] = [x for x in rows if x[0] == oper or not oper]
    except Exception as er:
        msg = f'Ошибка выполнения запроса: {er.args}'
        print(msg)
        logging.error(msg)
        # raise

    return result

