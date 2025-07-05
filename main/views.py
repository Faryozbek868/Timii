from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    Course, Teacher, Location, ContactMessage, Category,
    SiteStats, Service, Testimonial, ContactInfo, FAQ
)

def home(request):
    featured_courses = Course.objects.filter(is_active=True, is_featured=True)[:3]
    
    # SiteStats xavfsiz olish
    try:
        stats = SiteStats.objects.first()
        if not stats:
            # Agar SiteStats mavjud bo'lmasa, default yaratish
            stats = SiteStats.objects.create(
                students_count=500,
                teachers_count=50,
                courses_count=30,
                experience_years=5
            )
    except:
        # Agar jadval mavjud bo'lmasa, None qo'yish
        stats = None
    
    # Boshqa modellarni ham xavfsiz olish
    try:
        services = Service.objects.filter(is_active=True)[:4]
    except:
        services = []
    
    try:
        testimonials = Testimonial.objects.filter(is_active=True)[:3]
    except:
        testimonials = []
    
    context = {
        'featured_courses': featured_courses,
        'stats': stats,
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'main/home.html', context)

def courses(request):
    try:
        courses = Course.objects.filter(is_active=True)
        featured_courses = Course.objects.filter(is_active=True, is_featured=True)
        categories = Category.objects.filter(is_active=True)
    except:
        courses = []
        featured_courses = []
        categories = []
    
    context = {
        'courses': courses,
        'featured_courses': featured_courses,
        'categories': categories,
    }
    return render(request, 'main/courses.html', context)

def teachers(request):
    try:
        teachers = Teacher.objects.filter(is_active=True)
        featured_teachers = Teacher.objects.filter(is_active=True, is_featured=True)
    except:
        teachers = []
        featured_teachers = []
    
    context = {
        'teachers': teachers,
        'featured_teachers': featured_teachers,
    }
    return render(request, 'main/teachers.html', context)

def locations(request):
    try:
        locations = Location.objects.filter(is_active=True)
        main_location = Location.objects.filter(is_active=True, is_main=True).first()
    except:
        locations = []
        main_location = None
    
    context = {
        'locations': locations,
        'main_location': main_location,
    }
    return render(request, 'main/locations.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            ContactMessage.objects.create(
                name=name,
                surname=surname,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz.")
        except Exception as e:
            messages.error(request, "Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.")
        
        return redirect('main:contact')
    
    try:
        courses = Course.objects.filter(is_active=True)
        contact_info = ContactInfo.objects.first()
        faqs = FAQ.objects.filter(is_active=True)
    except:
        courses = []
        contact_info = None
        faqs = []
    
    context = {
        'courses': courses,
        'contact_info': contact_info,
        'faqs': faqs,
    }
    return render(request, 'main/contact.html', context)

