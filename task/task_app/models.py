from django.db import models

# Create your models here.
CATEGORY = (('business','仕事'),('life','生活'),('other','その他'))
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    contact = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
    max_length= 50,
    choices=CATEGORY
    )
    def __str__(self) :
        return self.title