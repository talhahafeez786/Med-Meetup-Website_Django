from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomeView.as_view(), name="index"),
    path('sevices/', views.ServiceListView.as_view(), name="services"),
    path('sevices/<int:pk>/', views.ServiceDetailView.as_view(), name="service_details"),
    path('doctors/', views.DoctoreListView.as_view(), name="doctors"),
    path('doctors/<int:pk>', views.DoctorDetailView.as_view(), name="doctor_details"),
    path('faqs/', views.FaqListView.as_view(), name="faqs"),
    path('gallery/', views.GalleryListView.as_view(), name="gallery"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]