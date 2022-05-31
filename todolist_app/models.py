
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

    
class TaskList(models.Model):
    todo = 'To-Do'
    personal  = 'Personal'
    shopping = 'Shopping'
    wishlist = 'Wishlist'
    work = 'Work'

    CATEGORIES = (
        (todo,todo),
        (personal,personal),
        (shopping,shopping),
        (wishlist,wishlist),
        (work,work)
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=20, 
        choices=CATEGORIES, 
    )

    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self):
        return self.title


class TaskItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["due_date"]