from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from dashboard.models import Student, Teacher, User, Batch

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'password1',
            'password2'
        )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

class StudentSignUpForm(UserCreationForm):
    roll_no = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'password1',
            'password2'
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user, roll_no = self.cleaned_data.get('roll_no'))
        return user
