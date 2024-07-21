from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm  # Ensure this import is present
from .models import User
from django.contrib.auth.hashers import make_password, check_password

def home_view(request):
    return render(request, 'myapp/home.html')

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)  # Hash the password
            user.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/my_template.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    # Assuming you want to redirect to home after successful login
                    return redirect('home')
                else:
                    form.add_error(None, 'Invalid password')
            except User.DoesNotExist:
                form.add_error(None, 'User does not exist')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})
