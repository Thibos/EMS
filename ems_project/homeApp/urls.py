from django.conf.urls import url
from .import views
from .views import graph,loging,profile,dashboard

# urlpattens=[
#
#     url(r'^$',views.post_list,name='post_list'),
#
#
# ]

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^graph',graph),
    url(r'^loging',loging),
    url(r'^profile',profile),
    url(r'^dashboard',dashboard),


]
