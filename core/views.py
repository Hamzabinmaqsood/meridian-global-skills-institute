from django.shortcuts import render, redirect
from django.contrib import messages
from inquiries.forms import InquiryForm


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your inquiry has been submitted successfully. Our team will contact you soon.')
            return redirect('core:contact')
    else:
        form = InquiryForm()

    return render(request, 'core/contact.html', {'form': form})


def admissions(request):
    return render(request, 'core/admissions.html')


def ielts(request):
    return render(request, 'core/ielts.html')


def study_abroad(request):
    return render(request, 'core/study_abroad.html')


def leadership(request):
    return render(request, 'core/leadership.html')
