from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeTemplateViews(TemplateView):
    template_name = 'core/home.html'


def sample(request):
    return render(request, "core/sample.html")
