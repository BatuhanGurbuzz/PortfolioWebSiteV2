from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Category Name")

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    tagName = models.CharField(max_length=50, null=True, verbose_name="Programming Language Name")

    def __str__(self):
        return self.tagName

class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Project Name")
    description = models.TextField(blank=True, null=True, verbose_name="Project Description")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING, verbose_name="Project Category")
    tags = models.ForeignKey(Tag, null=True, on_delete=models.DO_NOTHING, verbose_name="Project Programming Language")
    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name="Projects Slug")
    project_url = models.URLField(verbose_name="Project URL Link", null=True)
    file_upload = models.ImageField(upload_to='project_images/', null=True, blank=True)


    def __str__(self):
        return self.name
