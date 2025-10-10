from django.db import models
from django.db.models import DateField
from django.views.decorators.csrf import csrf_exempt



# Create your models here.

class Tasks(models.Model):
    Priority_choices=[('High','High'),('Medium','Medium'),('Low','Low')]
    Status_choices=[('In Progress','In Progress'),('Pending','Pending'),('To Do','To Do'),('Task Done','Task Done')]

    Task_Name=models.CharField(max_length=100)
    Priority=models.CharField(max_length=20,choices= Priority_choices)
    Due_Date=models.DateField()
    Status=models.CharField(max_length=50,choices=Status_choices)
    Assigned_By=models.CharField(max_length=50)
    Working_Hours=models.IntegerField()
    Description=models.CharField(max_length=1000)
    Discussion=models.CharField(max_length=1000)
    Links=models.URLField()
    Attachments=models.URLField()

class Projects(models.Model):

    Priority_choices = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    Status_choices = [('In Progress', 'In Progress'), ('Pending', 'Pending'), ('To Do', 'To Do'),
                      ('Task Done', 'Task Done')]
    Active_choices=[('View','View'),('Edit','Edit'),('Delete','Delete')]

    Project_Name=models.CharField(max_length=100)
    Company_Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=1000)
    Assigned_to=models.CharField(max_length=50)
    Due_Date = models.DateField(null=True, blank=True)
    Est_Hour=models.IntegerField()
    Priority=models.CharField(max_length=20,choices=Priority_choices)
    Links = models.URLField()
    Attachments = models.URLField()
    Status = models.CharField(max_length=50,choices=Status_choices)
    Active=models.CharField(max_length=15,choices=Active_choices)

