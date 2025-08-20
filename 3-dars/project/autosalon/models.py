from django.db import models

class Brad(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    images = models.ImageField(upload_to='images/', null=True, blank=True)
    videos = models.FileField(upload_to='videos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    brad = models.ForeignKey(Brad, on_delete=models.CASCADE)

    def __str__(self):
        return self.title