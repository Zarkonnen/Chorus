from django.db import models
import datetime

class Chore(models.Model):
    TYPE_CHOICES = (
        ('A', 'Automatic'),
        ('R', 'Reported')
    )
    STATUSES = (
        ('D', 'Done'),
        ('U', 'Unimportant'),
        ('N', 'Needs Doing'),
        ('I', 'Important!'),
        ('V', 'Very Urgent!!!')
    )
    choreType = models.CharField(max_length=1, choices=TYPE_CHOICES, default='R')
    name = models.CharField(max_length=100)
    periodHours = models.IntegerField(default=168)
    status = models.CharField(max_length=1, choices=STATUSES, default='D')
    lastUpdated = models.DateTimeField(auto_now_add=True)
    
    def markAsDone(self):
        self.lastUpdated = datetime.datetime.now()
        self.status = 'D'
        self.save()
    
    def updateStatus(self, status):
        self.lastUpdated = datetime.datetime.now()
        self.status = status
        self.save()
    
    @property
    def doUrgency(self):
        if self.choreType == 'A':
            return (datetime.datetime.now() - self.lastUpdated).total_seconds() / 3600.0 / self.periodHours
        else:
            return {
                'D': 0,
                'U': 0.3,
                'N': 1.0,
                'I': 3.0,
                'V': 9.9
            }[self.status]
    
    @property
    def reportUrgency(self):
        if self.choreType == 'A':
            return -1
        else:
            return (datetime.datetime.now() - self.lastUpdated).total_seconds() / 3600.0 / self.periodHours * 5
    
    def __str__(self):
        return self.choreType + " " + self.name + " every " + str(self.periodHours) + "h"
    
    def __unicode__(self):
        return self.choreType + " " + self.name + " every " + str(self.periodHours) + "h"
