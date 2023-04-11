from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    RED = 'Red'
    BLUE = 'Blue'
    TEAM_CHOICES = [
        (RED, 'RED TEAM'),
        (BLUE, 'BLUE TEAM')
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.CharField(max_length=4, choices=TEAM_CHOICES)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content
