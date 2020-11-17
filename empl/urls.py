from django.urls import path

from . import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('vehicles/',views.vehicles,name='vehicles'),
    path('diesels/',views.diesels,name='diesels'),
    path('drivers/',views.drivers,name='drivers'),
    path('maintenance/',views.maintenance,name='maintenance'),



    # path('detail/<int:id>',views.details,name='details'),
    # path('edit/<int:id>',views.edit,name='edit'),
    # path('delete/<int:id>',views.delete,name='delete'),

]