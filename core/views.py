from django.shortcuts import render, redirect
from django.contrib import messages
from inquiries.forms import InquiryForm
from courses.models import Course
from testimonials.models import Testimonial
from faqs.models import FAQ

def home(request):
    featured_courses = Course.objects.filter(is_active=True, is_featured=True)[:3]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    faqs = FAQ.objects.filter(is_active=True)[:6]

    context = {
        'featured_courses': featured_courses,
        'testimonials': testimonials,
        'faqs': faqs,
    }

    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    selected_course = request.GET.get('course', '')

    if request.method == 'POST':
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your inquiry has been submitted successfully. Our team will contact you soon.')
            return redirect('core:contact')
    else:
        form = InquiryForm(initial={
            'course_interested': selected_course
        })

    return render(request, 'core/contact.html', {'form': form})


def admissions(request):
    return render(request, 'core/admissions.html')


def ielts(request):
    return render(request, 'core/ielts.html')


def study_abroad(request):
    return render(request, 'core/study_abroad.html')


def leadership(request):
    return render(request, 'core/leadership.html')
