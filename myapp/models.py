from django.db import models

# Create your models here.

class Subject(models.Model):
    subject = models.CharField(max_length=20)


class Teacher(models.Model):
    name = models.TextField()
    surname = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)


class Class(models.Model):
    num_class = models.CharField(max_length=10)


class Student(models.Model):
    full_name = models.ForeignKey(Class, on_delete=models.DO_NOTHING)


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    clas = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

class Grade(models.Model):
    grade = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
