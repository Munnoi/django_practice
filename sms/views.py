from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

'''
def home(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "sms_home.html", context)
'''
class Home(ListView):
    model = Student
    template_name = "sms_home.html"
    context_object_name = "students"
'''
def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentForm()
    return render(request, "sms_form.html", {"form": form})
'''
class Add(CreateView):
    model = Student
    fields = "__all__"
    template_name = "sms_form.html"
    success_url = reverse_lazy("home")

'''
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
''' 
class Edit(UpdateView):
    model = Student
    fields = "__all__"
    template_name = "sms_form.html"
    success_url = reverse_lazy("home")

'''
def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("home")

    return render(request, "sms_confirm_delete.html")
'''
class Delete(DeleteView):
    model = Student
    template_name = "sms_confirm_delete.html"
    success_url = reverse_lazy("home")