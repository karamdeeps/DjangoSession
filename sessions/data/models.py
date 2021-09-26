from django.db import models


class DataModel(models.Model):
    id = models.AutoField(primary_key=True)
    request_data = models.TextField(max_length=50000,null=True, blank=True)
    request_number = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    session_value = models.CharField(max_length=100, null=True, blank=True)
    session_create_time = models.DateTimeField(null=True, blank=True)
    activity_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.request_number

    class Meta:
        db_table = "data_table"
