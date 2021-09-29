from django.urls import path
from  .views import  index ,detail, AddDoctors, AddNurses, AddPatients



urlpatterns = [
    path('',index, name="index"),
    path('detail/<int:pk>',detail, name='detail'),
    path('doctor/registration',AddDoctors.as_view(), name='adddoctor'),
    path('nurse/register', AddNurses.as_view(), name = 'addnurse'),
    path('patient/registration',AddPatients.as_view(), name="addpatient")
]