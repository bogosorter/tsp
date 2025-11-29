from django.shortcuts import render
from .models import Submission

def submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})
