# Imports
from django.conf.urls import url

from .models import Course

from .views import ShowHome, SelectCourse, AddCourse, EditCourse, \
    SearchCourse, DeleteCourse

# Create urls for app course

urlpatterns = [
    url(r'^$', ShowHome.as_view(model = Course, template_name = 'course/home_page_catalog.html'),
    name = 'show-home'),
    url(r'^select_course/(?P<pk>\d+)/$', SelectCourse.as_view(model = Course,
    template_name = 'course/select_page_course.html'), name = 'select-course'),
    url(r'^add_course/$', AddCourse.as_view(template_name = 'course/add_page_course.html'),
    name='add-course'),
    url(r'^edit_course/(?P<pk>\d+)/$', EditCourse.as_view(model = Course, template_name = 'course/edit_page_course.html'),
    name = 'edit-course'),
    url(r'^search_course/$', SearchCourse.as_view(),
    name = 'search-course'),
    url(r'^delete_course/(?P<pk>\d+)/$', DeleteCourse.as_view(model = Course,
    template_name = 'course/delete_page_course.html'), name = 'delete-course')
]