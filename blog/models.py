from django.db import models

# Create Blog Model
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # puts name for blogs in admin page (more readable)
    def __str__(self):
        return self.title

    # shortens blog summary
    def summary(self):
        return self.body[:150]
    
    # makes publication date look prettier
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# Steps for initially creating a model
# Create Blog Model
# Create migration
# Migrate
# Add to the admin