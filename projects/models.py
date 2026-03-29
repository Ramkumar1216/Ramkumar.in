from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    problem_statement = models.TextField(blank=True)
    dataset_used = models.TextField(blank=True)
    tools = models.TextField(help_text="Tools separated by commas. E.g., Python, Excel, Power BI")
    key_insights = models.TextField(blank=True)
    business_result = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tools_list(self):
        return [t.strip() for t in self.tools.split(',')]
