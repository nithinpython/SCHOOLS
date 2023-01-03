from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Course(models.Model):
    programming = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

