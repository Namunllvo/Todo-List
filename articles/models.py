from django.db import models
from users.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)    # 완료여부확인
    completion_at = models.DateTimeField(auto_now=True) # 완료시간

    def __str__(self):
        return str(self.title)