from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    #path('removepunc',views.removepunc,name='removepunc')
    path('analyze',views.analyze,name='analyze')
]
