from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def home(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "sms_home.html", context)


def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentForm()
    return render(request, "sms_form.html", {"form": form})

def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentForm(instance=student)
    return render(request, "sms_form.html", {"form": form, "student": student})

def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("home")

    return render(request, "sms_confirm_delete.html")