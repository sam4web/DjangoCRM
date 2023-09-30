from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import Record
from core.forms import RecordForm


def index_view(request):
    records = Record.objects.filter(created_by=request.user)
    context = {"records": records}
    return render(request, "core/index.html", context)


@login_required
def add_record(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_by = request.user
            record.save()
            return redirect("core:index")
    else:
        form = RecordForm()
    context = {"title": "Add Record", "form": form}
    return render(request, "core/form.html", context)


@login_required
def edit_record(request):
    pass


@login_required
def record_view(request, pk):
    record = Record.objects.get(pk=pk)
    context = {"record": record}
    return render(request, "core/detail.html", context)
