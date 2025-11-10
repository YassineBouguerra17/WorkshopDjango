from django.shortcuts import render,get_object_or_404
from .models import CONFERENCE, SUBMISSION
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import conferenceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


def list_conferences(request):
    conf_list = CONFERENCE.objects.all()
    return render(request, "conference/liste.html", {"liste": conf_list})

class conferenceList(ListView):
    model = CONFERENCE
    context_object_name = "liste"
    template_name = "conference/liste.html"

class conferencedetail(DetailView):
    model = CONFERENCE
    context_object_name = "conference"
    template_name = "conference/detail.html"

class conferenceCreate(LoginRequiredMixin,CreateView):
    model = CONFERENCE
    template_name = "conference/form.html"
    #fields = "__all__"
    form_class = conferenceForm
    success_url = reverse_lazy("list_conferences")

class conferenceUpdate(LoginRequiredMixin,UpdateView):
    model = CONFERENCE
    template_name = "conference/form.html"
    #fields = "__all__"
    form_class = conferenceForm
    success_url = reverse_lazy("list_conferences")

class conferenceDelete(LoginRequiredMixin,DeleteView):
    model = CONFERENCE
    template_name = "conference/conference_confirm_delete.html"
    success_url = reverse_lazy("list_conferences")

    


class SubmissionListView(LoginRequiredMixin, ListView):
    model = SUBMISSION
    template_name = "submission/liste.html"     
    context_object_name = "liste"

    def get_queryset(self):
        qs = (SUBMISSION.objects
              .select_related("conference", "user")
              .filter(user=self.request.user))

        conf_id = self.request.GET.get("conference")
        if conf_id:
            qs = qs.filter(conference_id=conf_id)
        return qs
    
class submissionDetail(LoginRequiredMixin, DetailView):
    model = SUBMISSION
    context_object_name = "submission"
    template_name = "submission/details.html"

    def get_queryset(self):
        return SUBMISSION.objects.select_related("conference", "user").filter(user=self.request.user)
    
class submissionCreate(LoginRequiredMixin, CreateView):
    model = SUBMISSION
    template_name = "submission/form.html"   # keep this path exactly
    fields = ["title", "abstract", "keywords", "papers", "conference"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        if not form.instance.status:
            form.instance.status = "submitted"  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "list_submissions",
            kwargs={"conference_id": self.object.conference_id}
        )
    
class submissionUpdate(LoginRequiredMixin, UpdateView):
    model = SUBMISSION
    template_name = "submission/form.html"
    fields = ["title", "abstract", "keywords", "papers"]  

    def get_queryset(self):
        return SUBMISSION.objects.filter(
            user=self.request.user,
        ).exclude(status__in=["accepted", "rejected"])

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status in ["accepted", "rejected"]:
            raise PermissionDenied("Cette soumission n'est plus modifiable.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(
            "list_submissions",
            kwargs={"conference_id": self.object.conference_id}
        )