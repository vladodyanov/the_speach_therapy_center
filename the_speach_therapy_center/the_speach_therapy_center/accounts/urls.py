
from django.urls import path, include

from the_speach_therapy_center.accounts.views import SignUpUserView, SignInUserView, signout_user, ProfileDetailsView, \
    ProfileUpdateView, ProfileDeleteView, ProfileStaffUpdateView

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),
    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="details profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
            path("editstaff/", ProfileStaffUpdateView.as_view(), name="edit profile staff"),
            path("delete/", ProfileDeleteView.as_view(), name="delete profile")
        ]),
    )
)