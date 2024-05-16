from django.db import models

# Create your models here.
class Project(models.Model):
    tagname = models.CharField('Код проекта', max_length=50)

    def __str__(self) -> str:
        return self.tagname
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    partnumber = models.CharField('Артикул', max_length=200)
    price = models.FloatField('Цена')
    projects = models.ManyToManyField(Project)

    def __str__(self) -> str:
        return self.name + ' ' + self.partnumber
    
    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименование'




