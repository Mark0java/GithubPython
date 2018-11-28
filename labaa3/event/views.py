from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.


def search_form(request):
    return render(request, 'event/search.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            events = models.Event.objects.filter(name__icontains=q)
            tickets = []
            for ev in events:
                tickets.append(models.Ticket.objects.filter(event=ev))
            return render(request, 'event/result.html', {'events': events, 'query': q, 'tickets': tickets})
    return render(request, 'event/search.html', {'error': error})


def buy(request):
    error = False
    if 'q' in request.POST:
        q = request.POST['q']
        if len(q) == 0:
            error = True
        else:
            ticket = models.Ticket.objects.filter(seat=q, owner_id=None, booked_id=None)
            if len(ticket) == 0:
                return render(request, 'event/bought.html', {'error': error})
            ticket[0].owner = request.user
            ticket[0].save()
            return render(request, 'event/bought.html', {'query': q})
    return render(request, 'event/bought.html', {'error': error})


def book(request):
    error = False
    if 'q' in request.POST:
        q = request.POST['q']
        if len(q) == 0:
            error = True
        else:
            ticket = models.Ticket.objects.filter(seat=q, booked_id=None, owner_id=None)
            if len(ticket) == 0:
                return render(request, 'event/bought.html', {'error': error})
            ticket[0].booked = request.user
            ticket[0].save()
            return render(request, 'event/bought.html', {'query': q, "booked": True})
    return render(request, 'event/bought.html', {'error': error})


def profile(request):
    user = request.user
    tickets_bought = models.Ticket.objects.filter(booked_id=None, owner=user)
    tickets_booked = models.Ticket.objects.filter(booked=user, owner_id=None)
    if len(tickets_booked) == 0 and len(tickets_bought) == 0:
        return render(request, 'event/profile.html', {'error': True})
    return render(request, 'event/profile.html', {'user': user, 'tickets_bought': tickets_bought, 'tickets_booked': tickets_booked})


def dismiss(request):
    error = False
    if 'q' in request.POST:
        q = request.POST['q']
        if len(q) == 0:
            error = True
        else:
            ticket = models.Ticket.objects.filter(seat=q, booked_id=request.user.id)
            if len(ticket) == 0:
                return render(request, 'event/bought.html', {'error': error})
            ticket[0].booked = None
            ticket[0].save()
            return redirect('profile/')
    return render(request, 'event/bought.html', {'error': error})


def buy_booked(request):
    error = False
    if 'q' in request.POST:
        q = request.POST['q']
        if len(q) == 0:
            error = True
        else:
            ticket = models.Ticket.objects.filter(seat=q, booked_id=request.user.id)
            if len(ticket) == 0:
                return render(request, 'event/bought.html', {'error': error})
            ticket[0].owner = request.user
            ticket[0].booked = None
            ticket[0].save()
            return redirect('profile/')
    return render(request, 'event/bought.html', {'error': error})

