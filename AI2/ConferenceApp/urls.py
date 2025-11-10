from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    #path("liste/",views.list_conferences,name="list_conferences"),
    path("liste/",conferenceList.as_view(),name="list_conferences"),
    path("<int:pk>/",conferencedetail.as_view(),name="conferencedetail"),
    path("add/",conferenceCreate.as_view(),name="add_conference"),
    path("edit/<int:pk>/",conferenceUpdate.as_view(),name="edit_conference"),
    path("delete/<int:pk>/",conferenceDelete.as_view(),name="conference_delete"),


    path("submissions/add/", views.submissionCreate.as_view(), name="add_submission"),
    path(
        "conferences/<int:conference_id>/submissions/",
        SubmissionListView.as_view(),
        name="list_submissions",
    ),
    path("submissions/<str:pk>/edit/", submissionUpdate.as_view(), name="update_submission"),

    path("submissions/<str:pk>/", views.submissionDetail.as_view(), name="submission_detail"),
   
]









