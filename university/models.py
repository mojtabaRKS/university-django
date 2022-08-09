from pyexpat import model
from django.db import models
import django.contrib.auth.models as authModels
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class File(models.Model):
    path = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=20)
    size = models.IntegerField
    extension = models.CharField
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class User(models.Model):
    user = models.OneToOneField(authModels.User, on_delete=models.CASCADE)
    national_code = models.CharField(default=255)


class Course(models.Model):
    title = models.CharField(max_length=255)
    theorical_units = models.IntegerField(default=1)
    practical_units = models.IntegerField(default=0)
    price = models.IntegerField



class Term(models.Model):
    semi_year = models.CharField(max_length=20)
    start_date = models.DateField
    end_date = models.DateField


class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.BigIntegerField


class Student(models.Model):
    user = models.ForeignKey(authModels.User, on_delete=models.CASCADE)


class Staff(models.Model):
    user = models.ForeignKey(authModels.User, on_delete=models.CASCADE)


class Presentation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    term
    status = models.CharField
    code = models.IntegerField
    day = models.CharField
    presentation_type = models.CharField(choices=('in-person', 'online'))
    class_type = models.CharField(choices=('compensational', 'general', 'professional', 'main'))
    exam_at = models.DateTimeField


class Session(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    start_at = models.DateTimeField
    end_at = models.DateTimeField


class StudentSession(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


class UserTerm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)


class Exam(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    file = 


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField
    status = models.CharField(choices=('passed', 'rejected', 'deleted'))
    exam_file = GenericForeignKey('File')
    