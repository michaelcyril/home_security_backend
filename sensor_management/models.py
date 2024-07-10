from django.db import models
import uuid


class IntruderAttempt(models.Model):
    STATUS = (
        (0, "OFF"),
        (1, "ON")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pir = models.IntegerField(choices=[(1, 'PIR1'), (2, 'PIR2'), (3, 'PIR3'), (4, 'PIR4')], default=1)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'intruder_attempts'
