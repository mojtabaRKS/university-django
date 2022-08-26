from core.utils.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class User(AbstractUser):
    """Custome user base on django best practice

    Args:
        AbstractUser (Class): base on defualt django class
    """

    national_code = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class File(BaseModel):
    path = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=20)
    size = models.IntegerField()
    extension = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Course(BaseModel):
    title = models.CharField(max_length=255)
    theorical_units = models.IntegerField(default=1)
    practical_units = models.IntegerField(default=0)
    price = models.IntegerField()


class Term(BaseModel):
    semi_year = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()


class Professor(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.BigIntegerField()


class Presentation(BaseModel):
    CLASS_TYPE = (
        ("COMPENSATIONAL", "compensational"),
        ("GENERAL", "general"),
        ("PROFESSIONAL", "professional"),
        ("MAIN", "main"),
    )
    PRESENTATION_TYPE = (
        ("IN_PERSON", "in_person"),
        ("ONLINE", "online"),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    term = models.IntegerField()
    status = models.CharField(max_length=255)
    code = models.IntegerField()
    day = models.CharField(max_length=255)
    presentation_type = models.CharField(max_length=50, choices=CLASS_TYPE)
    class_type = models.CharField(max_length=50, choices=(CLASS_TYPE))
    exam_at = models.DateTimeField()


class Session(BaseModel):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()


class StudentSession(BaseModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


class UserTerm(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)


class Exam(BaseModel):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)


class UserCourse(BaseModel):
    STATUS = (
        ("PASSED", "passed"),
        ("REJECTED", "rejected"),
        ("DELETED", "deleted"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
    status = models.CharField(max_length=255, choices=STATUS)
