from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Folder(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder_title = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.folder_title) + " | " + str(self.owner.id)
    

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete = models.CASCADE)
    file_name = models.CharField(max_length=255, blank=True)
    file = models.FileField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file) + " | " + str(self.folder)