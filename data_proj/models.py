from django.db import models

class DataProj(models.Model):
    proj_title = models.CharField()
    image = models.ImageField(upload_to='images/')
    summary = models.CharField()
    github = models.CharField()
    devpost = models.CharField()

    # puts name for blogs in admin page (more readable)
    def __str__(self):
        return self.proj_title