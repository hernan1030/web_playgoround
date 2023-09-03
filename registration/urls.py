from django.urls import path
from .views import SignUpView, ProfileUpdateViews, EmailUpdateViews


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdateViews.as_view(), name="profile"),
    path('profile/email/', EmailUpdateViews.as_view(), name="profile_email"),
]
