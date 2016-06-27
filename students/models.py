from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    """
    Class represents school
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    """
    Class represents classroom,
    It belongs to one school
    """
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    Class represents student,
    It belongs to one classroom
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
