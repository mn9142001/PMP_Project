from django.contrib import admin
from App.models import Comment, Lesson, Question, Answer , Topic , Exam , Course ,User
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'related_to','answer_texts')
    list_filter = ('topic','exam',)
    search_fields = ('text',)



    inlines = [AnswerInline]

    def related_to(self, obj):
        if obj.topic:
            return f" at : {obj.topic}"
        elif obj.exam:
            return f" at  : {obj.exam}"
        else:
            return obj.text
        
    def answer_texts(self, obj):
        answer_texts = []
        for i, answer in enumerate(obj.answer_set.all()):
            answer_text = format_html('{}{} {}', chr(i + 97), ')', answer.text)
            if answer.is_correct:
                answer_text = format_html('<span style="color: green;font-weight:900">{}</span>', answer_text)
            else :
                answer_text = format_html('<span style="color: red;f">{}</span>', answer_text)

            answer_texts.append(answer_text)
        return mark_safe(", ".join(answer_texts))


admin.site.register(Question, QuestionAdmin)





class TopicInline(admin.StackedInline):
    model = Topic
    extra = 0

class ExamInline(admin.StackedInline):
    model = Exam
    extra = 0

class LessonsInline(admin.StackedInline):
    model = Lesson
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    
    inlines = [LessonsInline,TopicInline,ExamInline]

admin.site.register(Course, CourseAdmin)



class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user','text', 'lesson')
    list_filter = ('lesson',)
    

admin.site.register(Comment, CommentsAdmin)


