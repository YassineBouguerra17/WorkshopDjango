from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    #path("liste/",views.list_conferences,name="list_conferences"),
    path("liste/",conferenceList.as_view(),name="list_conferences"),
    path("<int:pk>/",conferencedetail.as_view(),name="conferencedetail"),
    path("add/",conferenceCreate.as_view(),name="add_conference"),
]