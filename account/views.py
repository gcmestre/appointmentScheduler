from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import auth_login
from home.views import index


# Create your views here.
def register(request):
    print("register" + request.method)
    if request.method != "POST":
        form = UserCreationForm
        template = 'registration/register.html'
    else:
        user_creation_form = UserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            print("data is valid")
            new_user = user_creation_form.save()
            auth_login(request, new_user)
            return redirect(index)
        else:
            template = 'registration/register.html'
            form = user_creation_form

    context = {
        'form': form
    }

    return render(request, template, context=context)
