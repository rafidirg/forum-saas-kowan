from django.shortcuts import render


# Renders the main page from template
def home(request):
    return render(request, 'landing/home.html')
