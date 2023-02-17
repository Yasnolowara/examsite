from django.shortcuts import render, redirect
from register.forms import CreateUserForm


def registerPage(request):


    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'register/register.html', context)
