from django.core.exceptions import BadRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView
from faker import Faker

from core.forms import StudentForm
from core.models import Student


class StudentsView(ListView):
    template_name = "index.html"
    model = Student


class GenerateStudentView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        fake = Faker()
        Student.objects.create(
            name=fake.name(),
            age=fake.random_int(min=0, max=100),
            email=fake.email()
        )
        return redirect("/students/")


class GenerateStudentsCountView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        count = self.validate(request)
        fake = Faker()
        for i in range(count):
            Student.objects.create(
                name=fake.name(),
                age=fake.random_int(min=0, max=100),
                email=fake.email()
            )
        return redirect("/students/")

    def validate(self, request):
        try:
            count = int(request.GET.get("count"))
            if 0 <= count <= 100:
                return count
            raise BadRequest("The number does not satisfy the condition")
        except ValueError:
            raise BadRequest("The number does not satisfy the condition")


class CreateStudentView(FormView):
    template_name = "create-student.html"
    form_class = StudentForm
    success_url = "/students/"

    def form_valid(self, form):
        form.save()
        return super(CreateStudentView, self).form_valid(form)

