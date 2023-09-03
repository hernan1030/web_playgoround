from django.urls import path
from . import views
from .views import HomeTemplateViews

urlpatterns = [
    path('', HomeTemplateViews.as_view(), name="home"),

]
