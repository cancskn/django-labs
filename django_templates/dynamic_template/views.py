import datetime
from django.shortcuts import render

# Create your views here.
def weekday_view(request):
    day = datetime.datetime.now().strftime("%A")
    return render(request, "weekdays.html", {"day": day})