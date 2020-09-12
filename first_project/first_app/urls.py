from django.conf.urls import url
from django.conf.urls.static import static
from first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index')
] 
