from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import validate_comma_separated_integer_list


# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    graph = models.ImageField(upload_to='graph', null=True)
    x = models.CharField(validators=[validate_comma_separated_integer_list],max_length=50, null=True)
    y = models.CharField(validators=[validate_comma_separated_integer_list],max_length=50, null=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
