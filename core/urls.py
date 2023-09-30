from django.urls import path
from core.views import *

app_name = "core"


urlpatterns = [
    path("", index_view, name="index"),
    path("add/", add_record, name="add-record"),
    path("detail/<int:pk>", record_view, name="record-detail"),
]
