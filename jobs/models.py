from account.models import User
from django.db import models


class Jobs(models.Model):
    title = models.CharField(max_length=255)
    description =  models.TextField()
    num_workers = models.IntegerField()

    job_user = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    job_create_time = models.DateTimeField(auto_now_add=True)
    job_modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Application(models.Model):

    job = models.ForeignKey(Jobs, related_name='applications', on_delete=models.CASCADE)

    aadhaar_id = models.BigIntegerField(default=0)
    age = models.BigIntegerField(default=0)
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)










