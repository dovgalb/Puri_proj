from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display =['name', 'topic', 'number_of_questions', 'time']
    
class AnswerInline(admin.TabularInline):
    model = Answer
    filter_horizontal =['text',]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
    


    
