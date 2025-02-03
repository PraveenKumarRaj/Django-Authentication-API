from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response


from .models import Jobs
from .forms import JobForm, ApplicationForm


def job_card(request, job_id):
    job = Jobs.objects.get(pk=job_id)

    return render(request, 'board/job_card.html', {'job': job})


@login_required
def apply_job(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            return redirect('dashboard')
    
    else:
        form = ApplicationForm()

    return render(request, 'board/apply_job.html', {'form': form, 'job': job})


@login_required
def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)
            job.job_user = request.user
            form.save(commit=False)
            job.save()

            return redirect('dashboard')
        
    else:
        form = JobForm()
        
    
    return render(request, 'board/add_job.html', {'form': form})

