from django.shortcuts import render
from django.http import HttpResponse

# def main(request):
#     return HttpResponse("<h1 style='color:darkblue;'>Welcome to the City!</h1>")

# def news(request):
#     return HttpResponse("<h1 style='color:blue;'>Latest City News</h1>")

# def administration(request):
#     return HttpResponse("<h1 style='color:navy;'>City Administration Portal</h1>")

# def facts(request):
#     return HttpResponse("<h1 style='color:blueviolet;'>Interesting City Facts</h1>")

# def contacts(request):
#     return HttpResponse("<h1 style='color:indigo;'>Contact the City Officials</h1>")

# def history_main(request):
#     return HttpResponse("<h1> City History Overview </h1>")

# def history_people(request):
#     return HttpResponse("<h1> Historical People of the City </h1>")

# def history_photos(request):
#     return HttpResponse("<h1> Historical Photos of the City </h1>")


# Views with links
def main(request):
    return HttpResponse(
        """
        <h1 style='color:darkblue;'>Welcome to the City!</h1>
        <a href="/news">News</a> |
        <a href="/administration">Administration</a> |
        <a href="/facts">Facts</a> |
        <a href="/contacts">Contacts</a> |
        <a href="/history">History</a>               
        """
        )

def news(request):
    return HttpResponse(
        """
        <h1 style='color:blue;'>Latest City News</h1>
        <a href="/administration">Administration</a> |
        <a href="/facts">Facts</a> |
        <a href="/contacts">Contacts</a> |
        <a href="/history">History</a>  |
        <a href="/">Main</a>
        """
        )

def administration(request):
    return HttpResponse(
        """
        <h1 style='color:navy;'>City Administration Portal</h1>
        <a href="/news">News</a> |
        <a href="/facts">Facts</a> |
        <a href="/contacts">Contacts</a> |
        <a href="/history">History</a> |
        <a href="/">Main</a>
        """
        )

def facts(request): 
    return HttpResponse(
        """
        <h1 style='color:blueviolet;'>Interesting City Facts</h1>
        <a href="/news">News</a> |
        <a href="/administration">Administration</a> |
        <a href="/contacts">Contacts</a> |
        <a href="/history">History</a> |
        <a href="/">Main</a>
        """)

def contacts(request):
    return HttpResponse(
        """
        <h1 style='color:indigo;'>Contact the City Officials</h1>
        <a href="/news">News</a> |
        <a href="/facts">Facts</a> |
        <a href="/administration">Administration</a> |
        <a href="/history">History</a> |
        <a href="/">Main</a>
        """
        )

def history_main(request):
    return HttpResponse(
        """
        <h1> City History Overview </h1>
        <a href="/history/people">Historical People</a> |
        <a href="/history/photos">Historical Photos</a> |
        <a href="/news">News</a> |
        <a href="/facts">Facts</a> |
        <a href="/administration">Administration</a> |
        <a href="/">Main</a>
        """
        )

def history_people(request):
    return HttpResponse(
        """
        <h1> Historical People of the City </h1>
        <a href="/history/photos">Historical Photos</a> |
        <a href="/history">History</a>
        """
        )

def history_photos(request):
    return HttpResponse(
        """
        <h1> Historical Photos of the City </h1>
        <a href="/history/people">Historical People</a> |
        <a href="/history">History</a>
        """
        )