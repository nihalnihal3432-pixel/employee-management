from django.urls import path
from .views import (add_employee,emp_details,edit_employee,delete_employee)

urlpatterns = [
     path('',emp_details,name='empl'),
    path('add',add_employee,name='adde'),
    path('edit/<int:id>/',edit_employee,name='editt'),
    path('delete/<int:id>/',delete_employee,name='dellt'),
    
]