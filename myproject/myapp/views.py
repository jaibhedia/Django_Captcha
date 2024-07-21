from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Ensure this import is present

def home_view(request):
    return render(request, 'myapp/home.html')

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'myapp/my_template.html', {'form': form})

def login_view(request):
    return render(request, 'myapp/login.html')
