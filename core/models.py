from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)

    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="author", on_delete=models.CASCADE
    )

    def __str__(self):
        record_name = str(self.name)[0:15].lower().replace(" ", "_")
        str_rep = f"{record_name}__{self.created_at}"
        return str_rep

    class Meta:
        ordering = ("-modified_at",)
