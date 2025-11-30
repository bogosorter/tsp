from django.shortcuts import render
from .models import Submission

def home(request):
    submissions = Submission.objects.all()
    return render(request, 'home.html', {'submissions': submissions})
