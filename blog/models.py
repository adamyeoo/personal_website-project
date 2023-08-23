from django.db import models

# Create Blog Model
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Create migration

# Migrate

# Add to the admin