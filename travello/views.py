from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'the city that never sleeps'
    dest1.price = 900
    return render(request,"index.html",{'dest1':dest1})