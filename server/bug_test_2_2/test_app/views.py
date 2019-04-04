from django.shortcuts import render
from .models import *
from django.forms import modelformset_factory, inlineformset_factory

# Create your views here.
def index(request):
    SkillFormSet = modelformset_factory(Skill, extra=1, fields=('name','people'))
    formset = SkillFormSet(queryset = Skill.objects.all())

    if request.method == "POST":
        print (request.POST)
        formset = SkillFormSet(request.POST)
        formset.save()
        formset = SkillFormSet(queryset = Skill.objects.all())


    print (formset)
    return render(request, 'test_app/index.html', {"formset" : formset})
