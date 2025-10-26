import re
from webbrowser import get
from django.shortcuts import redirect, render, get_object_or_404
from .models import Person

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        Person.objects.create(name=name, surname=surname, email=email)

        print(f"Name: {name}, Surname: {surname}, Email: {email}")
        return redirect("/")
    return render(request, 'index.html')

def get_data(request):
    data = Person.objects.all()
    return render(request, 'data.html', {'data': data})

def delete_data(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return redirect('/')

def update_data(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        person.email = request.POST.get('email')
        person.save()
        return redirect('/')
    return render(request, 'update.html', {'person': person})

