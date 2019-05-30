from django.shortcuts import render
from .models import *
from .forms import *
from django.forms import modelformset_factory, inlineformset_factory


# Create your views here.
def index(request):
    LanguageFormSet = modelformset_factory(Language, extra=1, fields=('mother_tongue','person'))
    # InlineBFormset = inlineformset_factory(TestModel, Language,formset=LanguageFormSet, form=Language, extra=1)
    # formset = InlineBFormset(request.POST or None, instance=TestModel.objects.get(pk = 1))
    formset = AccountFormInline(request.POST or None, instance=Account.objects.get(pk=1))

    # formset = SkillFormSet(queryset = Skill.objects.all())
    #
    # if request.method == "POST":
    #     print (request.POST)
    #     formset = SkillFormSet(request.POST)
    #     formset.save()
    #     formset = SkillFormSet(queryset = Skill.objects.all())


    print (formset)
    return render(request, 'test_app/index.html', {"formset" : formset})
