from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(TestModel)
# admin.site.register(Language)
# admin.site.register(Skill)

# in admin.py

class AccountInline(admin.TabularInline):
    model = models.Account

    def get_fieldsets(self, request, obj=None):
        print ("-----From Account inline---------")
        print(repr(obj)) # => <Customer>
        print ("---------------------------------")
        """
        if obj and obj.account_type == 1:
            return ((None, {'fields': ('account_type', 'a')}),)
        elif obj and obj.account_type == 2:
            return ((None, {'fields': ('account_type', 'b')}),)
        """
        return ((None, {'fields': ('account_type',)}),)

    def get_fields(self, request, obj=None):
        print ("-----From Account field inline---------")
        print(repr(obj)) # => <Customer>
        print ("---------------------------------")
        """
        if obj and obj.account_type == 1:
            return ((None, {'fields': ('account_type', 'a')}),)
        elif obj and obj.account_type == 2:
            return ((None, {'fields': ('account_type', 'b')}),)
        """
        form = self._get_form_for_get_fields(request, obj)
        return [*form.base_fields, *self.get_readonly_fields(request, obj)]


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = (AccountInline,)

@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        print ("-----From Account admin----------")
        print(repr(obj)) # => <Account>
        print ("---------------------------------")
        if obj and obj.account_type == 1:
            return ((None, {'fields': ('account_type', 'a')}),)
        elif obj and obj.account_type == 2:
            return ((None, {'fields': ('account_type', 'b')}),)
        return ((None, {'fields': ('account_type',)}),)
