from django.db import models


class Application(models.Model):
    public_id = models.CharField(unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'applications'