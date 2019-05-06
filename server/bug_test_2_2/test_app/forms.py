from django.forms import ModelForm

class LanguageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.instance.related_field)
