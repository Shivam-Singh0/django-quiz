from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from ..models import Question, Score


@login_required
def index(request):

    user = request.user
    try:
        user_score = Score.objects.get(user=user)
    except:
        user_score = None
    if user_score:
        return redirect('result')
    else:
        questions = Question.objects.all()
        if request.method == 'POST':
            total = 0
            correct = 0
            for q in questions:
                if q.ans == request.POST.get(q.question):
                    total += 10
                    correct += 1
            incorrect = len(questions) - correct
            score = Score.objects.create(user=user, score=total,
                                         correct=correct, incorrect=incorrect)
            score.save()
            return redirect('result')
        else:

            return render(request, 'index.html', {'questions': questions})


@login_required
def results(request):
    user = request.user
    score = Score.objects.get(user=user)
    scores = Score.objects.order_by('-score')

    return render(request, 'results.html', {'score': score, 'scores': scores})
