from django.shortcuts import render
from celery import chain
from .tasks import *


def index(request):
    workflow = chain(test.s('diego'))
    workflow.delay()
    return render(request, 'index.html', {})
