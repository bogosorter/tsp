from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Submission
from .evaluator import evaluate_text

def home(request):
    submissions = Submission.objects.all()
    return render(request, 'home.html', {'submissions': submissions})

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        solution = request.POST.get('solution')

        if not name or not solution:
            return render(request, 'submit.html', {'error': 'Name and solution are required.', 'old': request.POST})

        try: score = evaluate_text(solution)
        except ValueError as e:
            return render(request, 'submit.html', {'error': str(e), 'old': request.POST})

        submission = Submission(name=name, score=score)
        submission.save()

        return redirect('home')

    return render(request, 'submit.html')
