from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"The current date and time is: {now}")

def multiplication_table(request):
    table = "<h1>Multiplication Table</h1><table border='1'>"
    for i in range(1, 11):
        table += "<tr>"
        for j in range(1, 11):
            table += f"<td>{i * j}</td>"
        table += "</tr>"
    table += "</table>"
    return HttpResponse(table)

def day_of_programmer(request):
    year = datetime.date.today().year
    day256 = datetime.date(year, 1, 1) + datetime.timedelta(days=255)
    return HttpResponse(f"The Day of the Programmer in {year} is on: {day256.strftime('%d %B %Y')}")
