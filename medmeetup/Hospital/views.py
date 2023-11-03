from typing import Any
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Slider, Service, Doctor, Faq, Gallery
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.

class HomeView(ListView):
    template_name = 'Hospital/index.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context ['sliders'] = Slider.objects.all()
        context ['experts'] = Doctor.objects.all()
        return context
    
class ServiceListView(ListView):
    template_name = 'Hospital/services.html'
    queryset = Service.objects.all()


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = 'Hospital/service_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['services'] = Service.objects.all()
        return context

class DoctoreListView(ListView):
    queryset = Doctor.objects.all()
    template_name = 'Hospital/team.html'
    paginate_by = 8 

class DoctorDetailView(DetailView):
    template_name = 'Hospital/team-details.html'
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['doctors'] = Doctor.objects.all()
        return context
    
class FaqListView(ListView) :
    template_name = 'Hospital/faqs.html'
    queryset = Faq.objects.all()

class GalleryListView(ListView):
    template_name = 'Hospital/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 9

class ContactView(TemplateView):
    template_name = 'Hospital/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        massage = request.POST.get('massage')
    
        if subject == '' :
            subject = "Med Meetup Contact"
        
        if name and email and massage and phone:
            send_mail(
                subject+"-"+phone,
                massage,
                email,
                ['expelmahmud@gmail.com'], 
                fail_silently= False
            )
            messages.success(request, "Email has been Sent successfully")
        
        return redirect('contact')