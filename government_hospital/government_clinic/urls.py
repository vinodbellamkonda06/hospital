from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'patient/',views.list_patient),

]