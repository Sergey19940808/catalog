# Imports
from django.conf.urls import url

from .models import Course

from .views import ShowHomePage, AddCourse

# Create urls for app course

urlpatterns = [
    url(r'^$', ShowHomePage.as_view(model = Course, template_name = 'course/home_page_catalog.html'), name = 'show-home'),
    url(r'^/add_course/$', AddCourse.as_view(model= Course, template_name = 'course/add_page_course.html'), name='add-course'),

]