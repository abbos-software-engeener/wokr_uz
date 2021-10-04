from django.urls import path

from api.views import *

app_name = "api"

urlpatterns =[
    path("",ShipperView.as_view()),
    path("ourservice/",OurServiceView.as_view()),
    path("career/",CareerView.as_view()),
    path("careeruser/<int:pk>/",CareerUserView.as_view()),
    path("aboutus/",AboutUsView.as_view()),
    path("carrier/",CarrierView.as_view()),
    path("contact/",ContactUserView.as_view()),


]