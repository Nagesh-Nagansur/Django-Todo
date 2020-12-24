from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

class Todos(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True ,max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



    # user=models.ForeignKey(CASC)
