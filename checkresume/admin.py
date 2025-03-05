from django.contrib import admin

# Register your models here.
from .models import Resume, ResumeDesciption

admin.site.register(Resume)
admin.site.register(ResumeDesciption)
