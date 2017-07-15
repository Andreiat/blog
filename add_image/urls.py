from django.conf.urls import url
from add_image import views

urlpatterns = [
    url(r'^$', views.add_image, name='add'),
]
