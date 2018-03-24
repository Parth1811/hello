from django.contrib import admin
from home_page.models import topics
from home_page.models import matsya_functions
#from home_page.forms import topicsForm

#class topicsAdmin(admin.ModelAdmin):
#    form = topicsForm

admin.site.register(topics)
admin.site.register(matsya_functions)
