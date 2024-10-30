from django.contrib import admin
from core.models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "teacher", "created_at"]
    list_filter = ["teacher"]
    search_fields = ["name", "description"]
    readonly_fields = ["created_at", "updated_at"]
    fields = ["name", "price", "description", "image", "teacher", "created_at", "updated_at"]
    