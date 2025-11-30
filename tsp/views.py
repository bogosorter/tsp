from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Submission

def home(request):
    submissions = Submission.objects.all()
    return render(request, 'home.html', {'submissions': submissions})

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        score = request.POST.get('score')

        submission = Submission(name=name, score=score)
        submission.save()

        return redirect('home')

    return render(request, 'submit.html')
