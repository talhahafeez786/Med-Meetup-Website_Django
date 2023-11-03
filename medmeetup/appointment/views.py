from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import View
from Hospital.models import Doctor
from .models import Appointment

# Create your views here.

class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'doctors' : Doctor.objects.all()
        }
        return render(request, "appointment/index.html", context)
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')

        if doctor_id:
            doctor = get_object_or_404(Doctor , id = doctor_id)
        
        if name and phone and email and doctor and date and time:
            Appointment.objects.create(
                name = name, phone= phone , email=email , doctor= doctor , date=date, time=time, note=note)
            messages.success(request, 'Appointment Done Succesfully')
        return redirect('appointment')
    
