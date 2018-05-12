from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    deadline = models.DateField()
    progress = models.IntegerField()

    def __str__(self):
        return self.title + '-' + self.description

    def update_todo(self, title, description, deadline, progress):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.progress = progress
        self.save()
    
    def get_color(self):
        if self.progress <= 30:
            return 'bg-danger'
        elif self. progress > 30 and self.progress <= 80:
            return 'bg-warning'
        else:
            return 'bg-success'