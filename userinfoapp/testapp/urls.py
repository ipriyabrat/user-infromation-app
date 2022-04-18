 
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('',views.home_view),
    path('dashbord/',views.dash_view),
    path('retrive/',views.retrive_view),
    path('insert/',views.insert_view),
    path('logout/',views.logout_view),
    path('signup/',views.signup_view),
    path('delete/<int:id>', views.delete_view),
    path('update/<int:id>', views.update_view),
    path('accounts/',include('django.contrib.auth.urls')),

]
