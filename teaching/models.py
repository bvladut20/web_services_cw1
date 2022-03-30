from django.db import models


class Professor(models.Model):
    code = models.CharField(max_length=5, blank=False, null=False)
    name = models.CharField(max_length=50)
    overall_rating = models.FloatField(null=True, blank=True)  # add Max and MinValueValidator
    number_ratings = models.IntegerField(default=0)
    total_ratings_sum = models.FloatField(default=0.0)

    def __str__(self):
        str_repr = self.name + " (" + self.code + ")"
        return str_repr


class Module(models.Model):
    code = models.CharField(max_length=5, blank=False, null=False)
    name = models.CharField(max_length=50)
    professors = models.ManyToManyField('Professor', blank=True)
    semester = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        str_repr = self.name + " (" + self.code + ") - " + str(self.year) + ", semester " + str(self.semester)
        return str_repr


class Rating(models.Model):
    value = models.FloatField(default=4)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)

    def __str__(self):
        str_repr = str(self.value) + " - " + str(self.professor) + " - " + str(self.module)
        return str_repr


