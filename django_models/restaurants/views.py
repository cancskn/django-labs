from unittest import result
from django.shortcuts import get_object_or_404, render, redirect

from .forms import RestaurantForm
from .models import Restaurant


# Create your views here.
def add_restaurant(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_restaurants")
    else:
        form = RestaurantForm()
    
    return render(request, "add_restaurant.html", {"form": form})

def list_restaurants(request):
    restaurants = Restaurant.objects.all()

    return render(request, "list_restaurants.html", {"restaurants": restaurants})


def delete_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, "delete_restaurants.html", {"restaurants": restaurants})

def delete_selected(request):
    if request.method == "POST":
        ids = request.POST.getlist("selected")
        Restaurant.objects.filter(id__in=ids).delete()
        return redirect("list_restaurants")
    return redirect("delete_page")

def edit_page(request):
    if request.method == "GET":
        # show the list
        restaurants = Restaurant.objects.all()
        return render(request, "edit_list.html", {"restaurants": restaurants})
    
    if request.method == "POST":
        # if a restaurant choosen
        selected_id = request.POST.get("selected")

        # show the edit form
        if selected_id and "save" not in request.POST:
            restaurant = Restaurant.objects.get(id=selected_id)
            form = RestaurantForm(instance=restaurant)
            return render(request, "edit_form.html", {"form": form, "restaurant_id": selected_id})

        # after save -> POST, save the changes
        if "save" in request.POST:
            restaurant = Restaurant.objects.get(id=request.POST.get("restaurant_id"))
            form = RestaurantForm(request.POST, instance=restaurant)
            if form.is_valid():
                form.save()
                return redirect("list_restaurants")

def search_restaurant(request):
    query = request.GET.get("q", "")
    results = Restaurant.objects.filter(specialization__icontains=query)
    return render(request, "search.html", {"results": results, "query": query})