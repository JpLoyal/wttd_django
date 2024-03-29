from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from eventex.core.models import Speaker, Talk

# Create your views here.

def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.filter(start__lt='12:00'),
        'afternoon_talks': Talk.objects.filter(start__gte='12:00'),
    }

    return HttpResponse('Aqui ficarão as palestras.', context)
