from django.db import models
import uuid

class Reading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trigger = models.IntegerField(null=True)
    pir1 = models.IntegerField()
    pir2 = models.IntegerField()
    pir3 = models.IntegerField()
    pir4 = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reading'