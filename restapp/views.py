from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm,LoginForm
from .models import Reservation,Customer,Tables,ReservTime,ReservState
from django.views.generic import ListView
# Create your views here.

def home(request):
    reservation = Reservation.objects.all().order_by('spot')
    return render(request,'index.html', {'reservation':reservation,'name': request.session.get('name'),'phone': request.session.get('phone')})

def reservation(request):
    reservation = Reservation.objects.all().order_by('spot')
    if request.method == 'GET':
        return render(request,'reservation.html',{'reservation':reservation,'name': request.session.get('name'),'phone': request.session.get('phone')})
    elif request.method == "POST":
        spot = request.POST['spot']
        time1 = request.POST['time']
        time2 = ReservTime.objects.get(pk=int(time1))
        table1 = request.POST['table']
        table2 = Tables.objects.get(pk=int(table1))
        party_num = request.POST['party_num']
        phone = request.session.get('phone')
        party = Customer.objects.get(pk=phone)
        reserv = ReservState.objects.get(pk=1)


        reservation1 = Reservation(
            spot = spot,
            party_num = party_num,
            table = table2,
            party = party,
            reserv = reserv,
            time = time2
            
        )
        reservation1.save()
        return render(request,'index.html',{'reservation':reservation,'name': request.session.get('name'),'phone': request.session.get('phone')})

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['name'] = form.name
        self.request.session['phone'] = form.phone
        return super().form_valid(form)

def update(request, reservation_id):
    reservation = Reservation.objects.all().order_by('spot')
    updates = get_object_or_404(Reservation, pk= reservation_id)
    if request.method == 'GET':
        return render(request,'update.html',{'reservation':reservation,'updates':updates})
        
    elif request.method == "POST":
        spot = request.POST['spot']
        time1 = request.POST['time']
        time2 = ReservTime.objects.get(pk=int(time1))
        table1 = request.POST['table']
        table2 = Tables.objects.get(pk=int(table1))
        party_num = request.POST['party_num']
        updates.spot = spot
        updates.time = time2
        updates.table = table2
        updates.party_num = party_num
        updates.save()
        return redirect('/')

def delete(request, reservation_id):
    deletes = get_object_or_404(Reservation, pk= reservation_id)
    deletes.delete()
    return redirect('/')
    