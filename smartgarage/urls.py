from django.urls import path
from smartgarage.views import *


urlpatterns = [
    path('userRegister/',user_register),
    path('userLogin/',user_login),
    path('getUsers/',get_all_users),
    path('updateUser/<int:id>',update_user),
    path('deleteUser/<int:id>',delete_user),
    path('adminRegister/',admin_register),
    path('adminLogin/',admin_login),
    path('getAdmins/',get_all_admins),
    path('updateAdmin/<int:id>',update_admin),
    path('deleteAdmin/<int:id>',delete_Admin),
    path('addGarage/',addgarage),
    path('getGarages/',get_all_garages),
    path('updateGarage/<int:id>',update_garage),
    path('deleteGarage/<int:id>',delete_garage),
    path('startReservation/',start_reservation),
    path('endReservation/',end_reservation),
    path('getUserCurrentReservation/<int:id>',getUserCurrentReservation),
    path('getUserReservation/<int:id>',getUserReservations),
    path('deleteReservation/<int:id>',delete_Rservation),
    path('getReservations/',get_all_reservation),
]
