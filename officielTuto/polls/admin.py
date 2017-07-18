from django.contrib import admin

# Register your models here.
# this gives admis the possibility to modify 
# data base related to my models 

from .models import Question
admin.site.register(Question)
