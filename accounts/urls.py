from django.urls import path
from .views import SignUpView, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/", ProfileDetailView.as_view(), name="profile"),
    path("<int:pk>/edit", ProfileUpdateView.as_view(), name="profile_edit"),
]