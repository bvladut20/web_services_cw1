from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=50)
    overall_rating = models.FloatField()  # add Max and MinValueValidator
    modules = models.ManyToManyField('Module')


class Module(models.Model):
    name = models.CharField(max_length=50)
    professors = models.ManyToManyField('Professor')
    semester = models.IntegerField()
    year = models.IntegerField()


class Rating(models.Model):
    value = models.FloatField
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)


