from django.shortcuts import render

# Create your views here.
def headphone(request):
    model = request.GET.get("model", "").lower()
    
    DATA = {
        "airpods": "Apple Airpod - wireless airpods from Apple",
        "budslive": "Samsung Galaxy Buds Live - noise cancelling technology",
        "bassxt": "Bass Airpod - perfect bass",
    }

    info = DATA.get(model, "Model not found")

    return render(request, "model.html", {"info": info})