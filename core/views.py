from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from core.forms import RecordForm, LoginForm, SignupForm
from core.models import Record


@login_required
def index_view(request):
    records = Record.objects.filter(created_by=request.user)
    context = {"records": records}
    return render(request, "core/index.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:index")
    else:
        form = LoginForm()

    context = {
        "title": "login",
        "btn_msg": "login",
        "form": form,
    }
    return render(request, "core/form.html", context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:login")
    else:
        form = SignupForm()

    context = {
        "title": "signup",
        "btn_msg": "signup",
        "form": form,
    }
    return render(request, "core/form.html", context)


@login_required
def logout_view(request):
    logout(request)
    return redirect("core:login")


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

    context = {
        "title": "add record",
        "btn_msg": "submit",
        "form": form,
    }
    return render(request, "core/form.html", context)


@login_required
def record_view(request, pk):
    record = Record.objects.get(pk=pk)
    context = {"record": record}
    return render(request, "core/detail.html", context)


@login_required
def edit_record(request, pk):
    record = Record.objects.get(pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("core:record-detail", pk=pk)
    else:
        form = RecordForm(instance=record)

    context = {
        "title": "edit record",
        "btn_msg": "Edit",
        "form": form,
    }
    return render(request, "core/form.html", context)


@login_required
def delete_record(request, pk):
    if request.method == "POST":
        record = Record.objects.get(pk=pk)
        record.delete()
        return redirect("core:index")
    context = {"id": pk}
    return render(request, "core/delete.html", context)
