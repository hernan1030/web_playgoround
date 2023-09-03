
from django.shortcuts import get_object_or_404

# vistas basadas en clase
from django.views.generic import ListView
from django.views.generic import DetailView

# modelos
from registration.models import Profile


# Create your views here.

class ProfileListViews(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 3


class ProfilesDetailViews(DetailView):

    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):

        return get_object_or_404(Profile, user__username=self.kwargs['username'])
