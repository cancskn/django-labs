from email import message
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .form_feed import FeedbackForm
from .form_book import BookReviewForm
from .form_info import SearchForm
from .form_search_page import SearchPageForm

# Create your views here.

def home_view(request):
    return render(request, "home.html")

def feedback_view(request):
    message = None

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = (
                f"Nickname: {data['nickname']}<br>"
                f"Email: {data['email']}<br>"
                f"Stars: {data['stars']}<br>"
                f"Experience: {data['description']}"
            )
        else:
            message = "Form is not valid."
    else:
        form = FeedbackForm()
    
    return render(request, "forms.html", {"form": form, "message": message})

def bookreview_view(request):
    message = None

    if request.method == "POST":
        form = BookReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            spoiler_text = "Yes" if data["contains_spoilers"] else "No"
            message = (
                f"Nickname: {data['nickname']}<br>"
                f"Rate: {data['rate']}<br>"
                f"Review: {data['review']}<br>"
                f"Contains spoilers: {spoiler_text}<br>"
            )
        else:
            message = "Form is not valid."
    else:
        form = BookReviewForm()
    
    return render(request, "forms.html", {"form": form, "message": message})

def load_people():
    people = []
    with open("people.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, city = line.split(",")
            people.append((name, city))
    return people

def search_view(request):
    message = None
    results = None

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]
            city = data["city"]

            people = load_people()
            results = people 
            
            if name:
                results = [p for p in results if name.lower() in p[0].lower()]
            if city:
                results = [p for p in results if city.lower() in p[1].lower()]

        else:
            message = "Form is not valid."
    else:
        form = SearchForm()
        
    return render(request, "forms.html", {"form": form, "message": message, "results": results})


def pagination_search(request):
    message = None

    # POST → GET redirect
    if request.method == "POST":
        form = SearchPageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]
            city = data["city"]
            return redirect(f"/pagesearch/?name={name}&city={city}")
        else:
            return render(request, "forms.html", {"form": form, "message": "Form invalid"})

    # GET
    name = request.GET.get("name", "")
    city = request.GET.get("city", "")
    form = SearchPageForm(initial={"name": name, "city": city})

    people = load_people()

    # Empty search → no results
    if not name and not city:
        results = []
    else:
        results = [
            p for p in people
            if (not name or name.lower() in p[0].lower()) and
               (not city or city.lower() in p[1].lower())
        ]

    paginator = Paginator(results, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "forms.html", {
        "form": form,
        "page_obj": page_obj,
        "name": name,
        "city": city,
    })