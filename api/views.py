from django.http import HttpResponse
from rest_framework import generics
from .serilizers import *
from App.models import Course, Lesson, Comment, Topic, Exam, Question, Answer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response



class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TopicListAPIView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicDetailAPIView(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetailAPIView(generics.RetrieveAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class RegisterView(generics.CreateAPIView):
    def get_serializer_class(self):
        return UserSerializer


    def post(self, request):
        user = request.data
        serializer = self.get_serializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        refresh = RefreshToken.for_user(serializer.instance)
        content = {
            "data": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Your User Created Successfully",
            "status": 200
        }
        return Response(content, status=status.HTTP_201_CREATED)


class CurrentUsers(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()