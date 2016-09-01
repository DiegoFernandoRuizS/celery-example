from django.shortcuts import render
from celery import chain
from .tasks import *


def index(request):
    workflow = chain(test.s('diego'))
    workflow.delay()

    workflow2 = chain(test2.s('algo'))
    workflow2.delay()
    return render(request, 'index.html', {})
