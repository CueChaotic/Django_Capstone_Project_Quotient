from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# All Views

def register(request):
    '''
    Checks form validity and saves the form data to the database.
    Redirects to the success page if the form is valid.
    '''
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_reg:reg_success")
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "new_user.html", context)

def register_success(request):
    '''
    Renders the success page.
    '''
    return render(request, "reg_success.html")

