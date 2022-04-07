from django.urls import path

from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView
from subscribapp.views import SubscriptionView

app_name = "subscribapp"

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(),name='subscribe'),
]
