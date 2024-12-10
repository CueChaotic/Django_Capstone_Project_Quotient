from django.shortcuts import render

# Create your views here.
def store_page(request):
    return render(request, "store_page.html")

