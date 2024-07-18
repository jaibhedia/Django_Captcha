from django.shortcuts import render
from .forms import MyForm  # Ensure the form is imported

def home_view(request):
    return render(request, 'myapp/home.html')

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            ...
    else:
        form = MyForm()

    return render(request, 'myapp/my_template.html', {'form': form})
