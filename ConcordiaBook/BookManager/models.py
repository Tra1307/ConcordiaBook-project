from django.db import models

# Create your models here.
class Textbooks(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length= 200)
    edition = models.CharField(max_length= 200, null=True, blank=True)
    condition = models.CharField(max_length=50, choices=[("New", "New"), ("Used", "Used"), ("Old", "Old"), ("Damaged", "Damaged")])
    course_code = models.CharField(max_length= 50)
    availability = models.BooleanField(default=True)


    #def __str__(self):
   #     return f"{self.title} ({self.course_code})"