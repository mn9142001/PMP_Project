from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver





@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def CreateToken(sender,created,instance,**kewargs):
    if created:
        Token.objects.create(user=instance)


class CustomUser(models.Model):
    user_name =models.CharField(max_length=100)
    email=models.EmailField()
    password = models.CharField(max_length=128)



    def __str__(self):
        return self.user_name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateField()
    image = models.ImageField(upload_to='course_images', blank=True, null=True)
    instructor=models.ForeignKey(User, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    trailer=models.FileField(upload_to='Courses_trailer_videos', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='lesson_videos', blank=True, null=True)
    pdf_file = models.FileField(upload_to='lesson_pdfs', blank=True, null=True)

    def __str__(self):
        return f"Lesson ( {self.name} ) , Course ( {self.course} )"

class Comment(models.Model):
    text = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} , Comment at {self.lesson}"

class Topic(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.name} , Course : {self.course}"


class Exam(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
        
    def __str__(self):
        return f"{self.name} , Course : {self.course}"
    

class Question(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True)
    QUESTION_TYPE_CHOICES = (
        ('MC', 'Multiple Choice'),
        ('OC', 'Only One Choice from Multi'),
        ('DD', 'Drag and Drop'),
    )
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE_CHOICES)


    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    text = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.text