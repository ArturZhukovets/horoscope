from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Dictionary
# Create your views here.


def dictionary(request):
    content = Dictionary.objects.all()
    context = {
        'content': content
    }
    return render(request, 'english_grammar_dictionary/index.html', context=context)

