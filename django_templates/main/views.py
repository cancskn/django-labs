from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def en(request):
    line = 'Hello, how are you?'
    return render(request, "translate.html", {"line": line})

def fr(request):
    line = 'Bonjour, comment allez-vous?'
    return render(request, "translate.html", {"line": line})

def de(request):
    line = "Hallo, wie geht es dir?"
    return render(request, "translate.html", {"line": line})

def es(request):
    line = "Hola, cómo estás?"
    return render(request, "translate.html", {"line": line})