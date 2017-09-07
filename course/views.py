# Imports
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView

from .models import Course

from .forms import AddCourseForm

from django.db.models import Q



# Create views with class-base-views
class ShowHome(ListView):
    context_object_name = 'courses'

    def get_queryset(self):
        courses = Course.objects.all()
        return courses


class SelectCourse(DetailView):
    context_object_name = 'course'

    def get_object(self, queryset=Course.objects.all()):
        object = super(SelectCourse, self).get_object()
        return object


class AddCourse(FormView):
    form_class = AddCourseForm
    success_url = reverse_lazy('show-home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.clean_name()
        form.clean_description()
        self.object.save()
        return super(AddCourse, self).form_valid(form)



class EditCourse(UpdateView):
    fields = ['name', 'description']
    context_object_name = 'course'

    def get_success_url(self, **kwargs):
        return reverse_lazy('select-course', kwargs={'pk': self.object.id})



class SearchCourse(View):
    template_name = 'course/search_page_course.html'


    def get(self, request):
        query = request.GET.get('query')

        if query:
            qset = (
                Q(name__startswith=query) |
                Q(description__startswith=query) |
                Q(date_added__startswith=query)
            )
            posts = Course.objects.filter(qset)

        else:
            posts = []

        return render(request, self.template_name, {'query': query, 'posts': posts})



class DeleteCourse(DeleteView):
    context_object_name = 'course'
    success_url = reverse_lazy('show-home')

    def get_template_names(self):
        return self.template_name

