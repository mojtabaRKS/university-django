from django.db import models
import django.contrib.auth.models as authModels


class User(models.Model):
    user = models.OneToOneField(authModels.User, on_delete=models.CASCADE)
    national_code = models.CharField(default=255)


class Course(models.Model):
    title = models.CharField(max_length=255)
    theorical_units = models.IntegerField(default=1)
    practical_units = models.IntegerField(default=0)


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(default=255)
    order = models.IntegerField(default=1)


class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.BigIntegerField


class Student(models.Model):
    user = models.ForeignKey(authModels.User, on_delete=models.CASCADE)


class Staff(models.Model):
    user = models.ForeignKey(authModels.User, on_delete=models.CASCADE)


class Presentation(models.Model):
    STATUSES = ("OPEN", "CANCEL", "")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    status = models.enums
    code = models.IntegerField