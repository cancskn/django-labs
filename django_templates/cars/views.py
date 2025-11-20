from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "main.html")

def toyota(request):
    return render(request, "toyota.html")

def honda(request):
    return render(request, "honda.html")

def renault(request):
    return render(request, "renault.html")