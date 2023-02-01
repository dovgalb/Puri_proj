from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DIFF_CHOICES = (
    ('simulator', 'simulator'),
    ('certification', 'certification'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название теста')
    topic = models.CharField(max_length=120, verbose_name='Тема теста')
    number_of_questions = models.PositiveSmallIntegerField(verbose_name='Количество вопросов')
    time = models.PositiveSmallIntegerField(help_text="Продолжительность теста в минутах")
    required_score_to_pass = models.PositiveSmallIntegerField(help_text='Количество очков в % для прохождения')
    difficulty = models.CharField(max_length=20, choices=DIFF_CHOICES)
    
    def __str__(self):
        return f'{self.name}-{self.topic}'

    def get_questions(self):
        return self.question_set.all()
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
     

class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    

class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст ответа')
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Вопрос: {self.question}, ответ: {self.text}, correct: {self.correct}" 
    
    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'
    
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.pk)
