from django.forms import ModelForm
from .models import Routine, Exercise

class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        exclude = ['created_timestamp']

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        exclude = ['routine']
