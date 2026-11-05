from django.contrib import admin
from cse.models import students
class studentsAdmin(admin.ModelAdmin):
    list_display=['name','study','phone']
admin.site.register(students,studentsAdmin)
# Register your models here.
