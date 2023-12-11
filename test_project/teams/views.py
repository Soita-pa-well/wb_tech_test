from django.shortcuts import render

from .models import Member


def index(request):
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'teams/index.html', context)
