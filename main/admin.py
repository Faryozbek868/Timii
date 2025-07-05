from django.contrib import admin
from .models import (
    Category, Course, Teacher, Location, ContactMessage, 
    SiteStats, Service, Testimonial, ContactInfo, FAQ
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'level', 'price', 'students_count', 'is_active', 'is_featured']
    list_filter = ['category', 'level', 'is_active', 'is_featured']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'is_featured']
    readonly_fields = ['created_at']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty', 'experience', 'students_count', 'rating', 'is_active', 'is_featured']
    list_filter = ['specialty', 'experience', 'is_active', 'is_featured']
    search_fields = ['name', 'specialty', 'bio']
    list_editable = ['is_active', 'is_featured']
    readonly_fields = ['joined_date']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', 'phone', 'capacity', 'is_active', 'is_main']
    list_filter = ['district', 'is_active', 'is_main']
    search_fields = ['name', 'address']
    list_editable = ['is_active', 'is_main']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'surname', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['created_at']

@admin.register(SiteStats)
class SiteStatsAdmin(admin.ModelAdmin):
    list_display = ['students_count', 'teachers_count', 'courses_count', 'experience_years']
    
    def has_add_permission(self, request):
        return not SiteStats.objects.exists()

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'rating', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['name', 'course', 'message']
    list_editable = ['is_active']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['phone_main', 'email_main']
    
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['question', 'answer']
    list_editable = ['is_active', 'order']
