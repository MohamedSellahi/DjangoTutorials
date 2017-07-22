import datetime 
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
"""
three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.


"""

# data base definition 
# Questions 

class Question(models.Model):
  question_text = models.CharField(max_length=255)
  pub_date = models.DateTimeField('date published')

  #the to string method
  def __str__(self):
    return self.question_text
  
  #custim method 
  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now



# Choice
class Choice(models.Model):
  question = models.ForeignKey(Question,on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=255)
  votes = models.IntegerField(default=0)
  
  def __str__(self):
    return self.choice_text


