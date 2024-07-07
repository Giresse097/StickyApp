from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=50)

    def mark_as_complete(self):
        self.status = True
        self.save()
        return "Completed!"

    def __str__(self):
        return f"{self.title} - Due: {self.due_date}"
