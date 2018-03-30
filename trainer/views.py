import logging
from django.shortcuts import redirect, render, get_object_or_404
from .models import Exercise, Routine
from .forms import RoutineForm, ExerciseForm

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        logger.debug('POST request received on form')
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            logger.info('Form validated. random_url = {}'.format(form_instance.random_url))
            return redirect('routine_detail', random_url=form_instance.random_url)
    else:
        logger.debug('GET request received on form')
        form = RoutineForm()
        return render(request, 'trainer/index.html', {'form': form})

def routine_detail(request, random_url):
    form = ExerciseForm()
    if request.method == 'POST':
        routine = get_object_or_404(Routine, random_url=random_url)
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.routine = routine
            form_instance.save()

    exercises = Exercise.objects.filter(routine__random_url = random_url)
    return render(request, 'trainer/routine_detail.html', {'exercises': exercises, 'form': form})
