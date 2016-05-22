from django.shortcuts import render, get_object_or_404
from django.http import Http404
from chorusp.chorus.models import *

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

def ui(request, list_slug, page):
    chores_list = get_object_or_404(ChoresList, slug=list_slug)

    if not request.user.is_authenticated() or not request.user in chores_list.users.all():
        raise Http404("Page does not exist.")
        
    if request.method == 'POST':
        chore = Chore.objects.get(id=int(request.POST['chore']))
        if request.POST['cmd'] == 'done':
            chore.markAsDone()
        elif request.POST['cmd'] == 'doneOn':
            chore.markAsDoneOn(request.POST['time_ago'])
        else:
            chore.updateStatus(request.POST['status'])

    rendered_chores_list = [(False, ch, importance(ch.doUrgency), ch.doUrgency) for ch in chores_list.chores.all()] + [(True, ch, importance(ch.reportUrgency), ch.reportUrgency) for ch in chores_list.chores.filter(choreType='R')]
    rendered_chores_list.sort(key=lambda tp: -tp[3])
    return render(request, page, context={'chores': rendered_chores_list, 'chores_list': chores_list, 'times_ago_list': Chore.TIMES_AGO})

def home(request):
    if not request.user.is_authenticated():
        raise Http404("Page does not exist.")
    
    return render(request, 'home.html', context={'chores_lists': request.user.chores_lists.all()})

def chores(request, list_slug):
    return ui(request, list_slug, "base.html")

def live(request, list_slug):
    return ui(request, list_slug, "live.html")
