from django.shortcuts import render
from models import *

def importance(v):
    if v < 0.1:
        return 'done'
    if v < 0.25:
        return 'very_unimportant'
    if v < 0.7:
        return 'unimportant'
    if v < 1.2:
        return 'todo'
    if v < 2:
        return 'important'
    if v < 4:
        return 'very_important'
    return 'urgent'

def ui(request, page):
    if request.method == 'POST':
        chore = Chore.objects.get(id=int(request.POST['chore']))
        if request.POST['cmd'] == 'done':
            chore.markAsDone()
        else:
            chore.updateStatus(request.POST['status'])
    chore_list = [(False, ch, importance(ch.doUrgency), ch.doUrgency) for ch in Chore.objects.all()] + [(True, ch, importance(ch.reportUrgency), ch.reportUrgency) for ch in Chore.objects.filter(choreType='R')]
    chore_list.sort(key=lambda tp: -tp[3])
    return render(request, page, context={'chores': chore_list})

def home(request):
    return ui(request, "base.html")

def live(request):
    return ui(request, "live.html")
