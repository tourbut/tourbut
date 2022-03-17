from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 10


@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:list')

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    #form_class = CommentCreationForm