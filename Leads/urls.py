from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls.conf import include


router = DefaultRouter()
router.register('productoperations',views.ProductView,basename="productoperations")

urlpatterns = [
    path('contact',views.CustomerView.as_view(),name="contact"),
    path('managecontact/<pk>',views.CustomerManagmentView.as_view(),name="managecontact"),
    path('contactlist/',views.CustomerListView.as_view(),name="contactlist"),
    path('api/',include(router.urls))

]
