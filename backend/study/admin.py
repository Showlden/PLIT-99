from django.contrib import admin

from .forms import StudyForm
from .models import Specialization, Course

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    form = StudyForm

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = StudyForm