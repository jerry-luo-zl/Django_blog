'''
===========================================================
This is the part for models defination 
===========================================================
'''

from django.db import models
from django.conf import settings
from django.utils import timezone
'''
===========================================================
The explanation of django.db,django.conf,and django.utils
unknown for now 
===========================================================
'''
class Post(models.Model):

    '''
    ===========================================================
    ForeignKey is a link to other things
    CharField is a limited text
    TextField is a unlimited text
    DateTimeField is a date and time
    ===========================================================
    '''

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title