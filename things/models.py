from django.db import models

#create model things
class Thing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
