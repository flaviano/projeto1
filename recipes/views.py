from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html',
                  context={
                      'name': 'Flaviano',
                      'age': 44
                  })
