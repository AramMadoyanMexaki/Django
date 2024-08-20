from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.result, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("register/", views.register, name="register"),
    path("login/", views._login, name="login"),
    path("logout/", views.log_out, name="logout"),
]
