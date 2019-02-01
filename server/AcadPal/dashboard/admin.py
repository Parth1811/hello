from django.contrib import admin
from dashboard.models import Batch, Teacher, Student, User

# Register your models here.
admin.site.register(Batch)
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
