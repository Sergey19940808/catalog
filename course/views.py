# Imports
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView

from .models import Course

from .forms import AddCourseForm



# Create views with class-base-views
class ShowHomePage(ListView):
    context_object_name = 'courses'

    def get_queryset(self):
        courses = Course.objects.all()
        return courses



class AddCourse(FormView):
    form_class = AddCourseForm
    success_url = reverse_lazy('show-home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.clean_name()
        form.clean_description()
        self.object.save()
        return super(AddCourse, self).form_valid(form)

