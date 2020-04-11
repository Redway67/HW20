from django import template
from datetime import date

register = template.Library()


# Возвращает количество дней до события, если событие в прошлом, то 0
def rest_day(book_date):
    return (book_date - date.today()).days if book_date > date.today() else 0


register.filter('rest_day', rest_day)
