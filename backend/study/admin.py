from django.contrib import admin

from .forms import StudyForm
from .models import Specialization, Course

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = "title term contract".split()
    list_filter = "title term contract".split()
    search_fields = "title term contract".split()

    form = StudyForm

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "title term price".split()
    list_filter = "title term price".split()
    search_fields = "title term price".split()

    form = StudyForm