from django.urls import path
from myapp import views


urlpatterns=[
    path('',views.index,name = 'index'),
    path('pictures/<int:pIndex>',views.pictures,name = 'pictures'),
    path('upload',views.upload,name = 'upload'),
    path('doupload',views.doupload,name='doupload'),
    path('edit/<int:uid>',views.edit,name= 'edit'),
    path('delete/<int:uid>',views.delete,name = 'delete'),

]