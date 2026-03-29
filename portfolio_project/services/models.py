from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='📊')  # emoji or icon class
    image = models.ImageField(upload_to='services/', null=True, blank=True)  # Service image
    features = models.TextField(help_text="Features separated by commas")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.title
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split(',')]
