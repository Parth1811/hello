from django.forms import ModelForm, BaseInlineFormSet
from . import models

class LanguageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.instance.related_field)

class AccountFormInline(BaseInlineFormSet):
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
