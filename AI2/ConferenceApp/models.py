from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
class CONFERENCE(models.Model):
    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(validators=[MaxLengthValidator(30, "Description must be at most 30 characters long.")])
    Theme_list = [
        ('CSAI', 'Computer Science & Artificial Intelligence'),
        ('SE', 'Science & Engineering'),
        ('SSE', 'Social Sciences & Education'),
        ('IT', 'Interdisciplinary Themes'),
    ]
    Theme = models.CharField(max_length=225,choices=Theme_list)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date.")    


class SUBMISSION(models.Model):
    submission_id = models.CharField(max_length=255,primary_key=True,unique=True)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.TextField()
    papers = models.FileField(upload_to='paper/')
    STATUS =[
        ('submitted','submitted'),
        ('under review', 'under review'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    ]
    status = models.CharField(max_length=50,choices=STATUS)
    payed = models.BooleanField(default=False)
    submission_date= models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('UserApp.USER',on_delete=models.CASCADE,related_name='submissions')
    conference = models.ForeignKey(CONFERENCE,on_delete=models.CASCADE,related_name='submissions')  
