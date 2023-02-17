from django.shortcuts import render, redirect
from register.forms import CreateUserForm


# from register.forms import CreaterUserForm


def index(requests):
    return render(requests, 'backend/index.html')


def categories(requests):
    return render(requests, 'backend/categories.html')


#
#
def checkout(requests):
    return render(requests, 'backend/check-out.html')


#
#
#
def contact(requests):
    return render(requests, 'backend/contact.html')
#
#
#
# def index(requests):
#     return render(requests, 'backend/index.html')
#
#
#
# def index(requests):
#     return render(requests, 'backend/index.html')
#
#
#
# def index(requests):
#     return render(requests, 'backend/index.html')
#
#
#
# def index(requests):
#     return render(requests, 'backend/index.html')
#
#
#
#

def registerPage(request):


    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'register/register.html', context)
