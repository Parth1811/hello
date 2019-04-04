from django.contrib import admin
from .models import TestModel, Language, Skill
# Register your models here.

admin.site.register(TestModel)
admin.site.register(Language)
admin.site.register(Skill)
