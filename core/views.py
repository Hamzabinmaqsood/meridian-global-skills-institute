from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def admissions(request):
    return render(request, 'core/admissions.html')


def ielts(request):
    return render(request, 'core/ielts.html')


def study_abroad(request):
    return render(request, 'core/study_abroad.html')


def leadership(request):
    return render(request, 'core/leadership.html')
