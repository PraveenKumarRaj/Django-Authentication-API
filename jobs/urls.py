from django.urls import path, include

from .views import add_job, job_card, apply_job


urlpatterns = [
    path('<int:job_id>/', job_card, name='job_card'),
    path('add/', add_job, name='add_job'),
    path('<int:job_id>/apply_job/', apply_job, name='apply_job')
]