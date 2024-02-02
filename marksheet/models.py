from django.db import models

# Create your models here.
class Semester(models.Model):
    title = models.CharField(max_length=50)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title

class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='semester_subject')
    
    title = models.CharField(max_length=50)
    code = models.PositiveIntegerField()
    credit = models.FloatField(max_length=5)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
