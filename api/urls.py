from django.urls import path, include
from api.views import (CourseListAPIView, CourseDetailAPIView, CurrentUsers, LessonListAPIView, 
                    LessonDetailAPIView, CommentListAPIView, CommentDetailAPIView, 
                    TopicListAPIView, TopicDetailAPIView, ExamListAPIView, ExamDetailAPIView, 
                    QuestionListAPIView, QuestionDetailAPIView, AnswerListAPIView, AnswerDetailAPIView,RegisterView)
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


router = routers.DefaultRouter()
# If you want to add additional endpoints for other views, you can register them with the router here

urlpatterns = [
    path('', include(router.urls)),
    
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),

    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    
    path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    
    path('topics/', TopicListAPIView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetailAPIView.as_view(), name='topic-detail'),
    
    path('exams/', ExamListAPIView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetailAPIView.as_view(), name='exam-detail'),
    
    path('questions/', QuestionListAPIView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    
    path('answers/', AnswerListAPIView.as_view(), name='answer-list'),
    path('answers/<int:pk>/', AnswerDetailAPIView.as_view(), name='answer-detail'),

    path('users/<int:pk>/', CurrentUsers.as_view(), name='answer-detail'),


    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/',RegisterView.as_view(),name="signup"),
    

]
