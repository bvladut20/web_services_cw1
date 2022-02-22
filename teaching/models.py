from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=50)
    overall_rating = models.FloatField(null=True, blank=True)  # add Max and MinValueValidator
    modules = models.ManyToManyField('Module', null=True, blank=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=50)
    professors = models.ManyToManyField('Professor', null=True, blank=True)
    semester = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    value = models.FloatField(default=4)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)

    def __str__(self):
        return self.value


