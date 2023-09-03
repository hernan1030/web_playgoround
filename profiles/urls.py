from django.urls import path
from .views import ProfileListViews, ProfilesDetailViews


urlpatterns = [
    path('', ProfileListViews.as_view(), name="list"),
    path('<username>', ProfilesDetailViews.as_view(), name="detail"),
]
