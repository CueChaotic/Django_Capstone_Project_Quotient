from django.shortcuts import render

# All views
def front_page(request):
    return render(request, 'front_page.html')

