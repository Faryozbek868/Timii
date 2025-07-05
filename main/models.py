from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    icon = models.CharField(max_length=50, default="fas fa-book", verbose_name="Icon")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan")
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', "Boshlang'ich"),
        ('intermediate', "O'rta"),
        ('advanced', "Yuqori"),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Tavsif")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Daraja")
    duration_months = models.IntegerField(default=3, verbose_name="Davomiyligi (oy)")
    students_count = models.IntegerField(default=0, verbose_name="O'quvchilar soni")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0, verbose_name="Reyting")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narx (so'm)")
    instructor = models.CharField(max_length=100, verbose_name="O'qituvchi")
    image = models.ImageField(upload_to='courses/', blank=True, verbose_name="Rasm")
    features = models.TextField(help_text="Har bir xususiyatni yangi qatordan yozing", verbose_name="Xususiyatlar")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    is_featured = models.BooleanField(default=False, verbose_name="Mashhur")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan")
    
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_features_list(self):
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]
    
    @property
    def duration(self):
        return f"{self.duration_months} oy"

class Teacher(models.Model):
    EXPERIENCE_CHOICES = [
        ('1-2', '1-2 yil'),
        ('3-5', '3-5 yil'),
        ('5-10', '5-10 yil'),
        ('10+', '10+ yil'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Ism Familiya")
    specialty = models.CharField(max_length=100, verbose_name="Mutaxassislik")
    bio = models.TextField(verbose_name="Biografiya")
    experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES, verbose_name="Tajriba")
    students_count = models.IntegerField(default=0, verbose_name="O'quvchilar soni")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0, verbose_name="Reyting")
    photo = models.ImageField(upload_to='teachers/', blank=True, verbose_name="Rasm")
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    skills = models.TextField(help_text="Har bir ko'nikmani yangi qatordan yozing", verbose_name="Ko'nikmalar")
    languages = models.TextField(help_text="Har bir tilni yangi qatordan yozing", verbose_name="Tillar")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    is_featured = models.BooleanField(default=False, verbose_name="Asosiy o'qituvchi")
    joined_date = models.DateField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    
    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
        ordering = ['-joined_date']
    
    def __str__(self):
        return f"{self.name} - {self.specialty}"
    
    def get_skills_list(self):
        return [skill.strip() for skill in self.skills.split('\n') if skill.strip()]
    
    def get_languages_list(self):
        return [language.strip() for language in self.languages.split('\n') if language.strip()]
    
    def get_experience_display(self):
        return dict(self.EXPERIENCE_CHOICES).get(self.experience, self.experience)

class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="Filial nomi")
    district = models.CharField(max_length=100, verbose_name="Tuman")
    address = models.TextField(verbose_name="Manzil")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="Email")
    working_hours = models.CharField(max_length=100, verbose_name="Ish vaqti")
    capacity = models.IntegerField(verbose_name="Sig'im")
    image = models.ImageField(upload_to='locations/', blank=True, verbose_name="Rasm")
    features = models.TextField(help_text="Har bir xususiyatni yangi qatordan yozing", verbose_name="Imkoniyatlar")
    transport = models.TextField(help_text="Har bir transport turini yangi qatordan yozing", verbose_name="Transport")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    is_main = models.BooleanField(default=False, verbose_name="Bosh filial")
    opened_date = models.DateField(auto_now_add=True, verbose_name="Ochilgan sana")
    
    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"
        ordering = ['-is_main', 'name']
    
    def __str__(self):
        return self.name
    
    def get_features_list(self):
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]
    
    def get_transport_list(self):
        return [transport.strip() for transport in self.transport.split('\n') if transport.strip()]

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    surname = models.CharField(max_length=100, verbose_name="Familiya")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    subject = models.CharField(max_length=200, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar")
    is_read = models.BooleanField(default=False, verbose_name="O'qilgan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")
    
    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} {self.surname} - {self.subject}"

# Statistics model for homepage
class SiteStats(models.Model):
    students_count = models.IntegerField(default=500, verbose_name="O'quvchilar soni")
    teachers_count = models.IntegerField(default=50, verbose_name="O'qituvchilar soni")
    courses_count = models.IntegerField(default=30, verbose_name="Kurslar soni")
    experience_years = models.IntegerField(default=5, verbose_name="Tajriba yillari")
    
    class Meta:
        verbose_name = "Sayt statistikasi"
        verbose_name_plural = "Sayt statistikasi"
    
    def __str__(self):
        return "Sayt statistikasi"

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Xizmat nomi")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.CharField(max_length=50, default="fas fa-star", verbose_name="Icon")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    order = models.IntegerField(default=0, verbose_name="Tartib")
    
    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    course = models.CharField(max_length=100, verbose_name="Kurs")
    message = models.TextField(verbose_name="Fikr")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5, verbose_name="Reyting")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan")
    
    class Meta:
        verbose_name = "Fikr"
        verbose_name_plural = "Fikrlar"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.course}"

class ContactInfo(models.Model):
    phone_main = models.CharField(max_length=20, verbose_name="Asosiy telefon")
    phone_secondary = models.CharField(max_length=20, blank=True, verbose_name="Qo'shimcha telefon")
    email_main = models.EmailField(verbose_name="Asosiy email")
    email_support = models.EmailField(blank=True, verbose_name="Yordam email")
    address = models.TextField(verbose_name="Manzil")
    working_hours = models.TextField(verbose_name="Ish vaqti")
    telegram = models.URLField(blank=True, verbose_name="Telegram")
    instagram = models.URLField(blank=True, verbose_name="Instagram")
    facebook = models.URLField(blank=True, verbose_name="Facebook")
    youtube = models.URLField(blank=True, verbose_name="YouTube")
    
    class Meta:
        verbose_name = "Aloqa ma'lumotlari"
        verbose_name_plural = "Aloqa ma'lumotlari"
    
    def __str__(self):
        return "Aloqa ma'lumotlari"

class FAQ(models.Model):
    question = models.CharField(max_length=200, verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    order = models.IntegerField(default=0, verbose_name="Tartib")
    
    class Meta:
        verbose_name = "Savol-Javob"
        verbose_name_plural = "Savol-Javoblar"
        ordering = ['order']
    
    def __str__(self):
        return self.question
