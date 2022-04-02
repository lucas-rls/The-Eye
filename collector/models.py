from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_session_timestamp", fields=["session_id", "timestamp"]
            )
        ]

    session_id = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)


class EventError(models.Model):
    message = models.CharField(max_length=300)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now=True)