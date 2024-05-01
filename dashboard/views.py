from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from main import models


def index(request):
    quizzes = models.Quiz.objects.filter(author=request.user.id)
    return render(request, 'index.html', {'quizzes':quizzes})



# --------------- Quiz list --------------------
def quiz_list(request):
    """ Quiz list """
    quizzes = models.Quiz.objects.all()
    return render(request, 'quiz/list.html', {'quizzes':quizzes})



# ------------ Quiz create --------------------
def quiz_create(request):
    """ Quiz create """
    if request.method == 'POST':
        name = request.POST.get('name')
        quiz = models.Quiz.objects.create(name=name, author=request.user)
        return redirect('quiz_detail', quiz.code)
    
    return render(request, 'quiz/create.html')



# --------------- Quiz detail -------------------
def quiz_detail(request, code):
    """ Quiz detail """
    quiz = models.Quiz.objects.get(code=code)
    questions = models.Question.objects.filter(quiz=quiz)
    context = {
        'quiz':quiz,
        'questions':questions
    }
    return render(request, 'quiz/detail.html', context)



# ---------------- Question create --------------
def question_create(request, code):
    """ Question create """
    quiz = models.Quiz.objects.get(code=code)
    if request.method == 'POST':
        question = models.Question.objects.create(
            name=request.POST['question'],
            quiz=quiz
            )
        models.Option.objects.create(
            name = request.POST['correct_option'],
            question = question,
            is_correct = True
        )
        for option in request.POST.getlist('options'):
            models.Option.objects.create(
            name = option,
            question = question,
            is_correct = False
            )
        return redirect('question_detail',question.code)
    return render(request,'question/create.html', {'quiz':quiz})



# ---------------- Question detail --------------
def question_detail(request, code):
    """ Question detail """
    question = models.Question.objects.get(code=code)
    options = models.Option.objects.filter(question=question)
    context = {
        'question':question,
        'options':options
    }
    return render(request, 'question/detail.html', context)



# ----------------- Question delete ----------------
def question_delete(request, code):
    """ Question delete """
    question = models.Question.objects.get(code=code)
    question.delete()
    return redirect('quiz_detail', question.quiz.code)



# ----------------- Question Update --------------------------------
def question_update(request, code):
    """ Question update """
    question = models.Question.objects.get(code=code)
    print(request.POST)
    if request.method == 'POST':
        question.name = request.POST['name']
        question.save()
        return redirect('question_detail', question.code)
    


# ----------------- Answer list --------------------------------
def answer_list(request, code):
    """ Answer list """
    answers = models.Answer.objects.filter(quiz__code = code)
    context = {'answers':answers}
    return render(request, 'answer_list.html', context)



# ------------------ Answer detail ------------------------
def answer_detail(request, code):
    """ Answer detail """
    answer = models.Answer.objects.get(code=code)
    details = models.AnswerDetail.objects.filter(answer=answer)
    correct = 0
    
    in_correct = 0
    for detatil in details:
        if detatil.is_correct:
            correct +=1
        else:
            in_correct +=1
    correct_percentage = int(correct * 100 / details.count())
    in_correct_percentage = 100 - correct_percentage

    context = {
        'answer':answer,
        'details':details,
        'correct':correct,
        'in_correct':in_correct,
        'total':details.count(),
        'correct_percentage':int(correct_percentage),
        'in_correct_percentage':in_correct_percentage
    }

    return render(request, 'answer_detail.html', context)



# ---------------------- Login --------------------------------
def log_in(request):
    """ Log in """
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    return render(request, 'auth/login.html')



# ------------------ Logout ---------------------------------
def log_out(request):
    """ Log out """
    logout(request)
    messages.success(request, 'logout success')
    return redirect('index')



"""
Quiz Create +++, List +++, Detail +++
Question Create +++, Detail ---
Option Create +++ ---
"""

