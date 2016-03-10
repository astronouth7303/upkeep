from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from .views import stuffindex, thing, AddThing, AddSchedule

urlpatterns = [
    url('^thing$', stuffindex, name='index'),
    url(r'^thing/add$', AddThing.as_view(), name='addthing'),
    url(r'^thing/(\d+)$', thing, name='thing'),
    url(r'^thing/(\d+)/add$', AddSchedule.as_view(), name='addschedule'),
]
