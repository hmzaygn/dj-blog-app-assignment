from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
