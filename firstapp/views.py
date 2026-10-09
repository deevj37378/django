from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

class HelloIndia(View):
    def get(self, request):
        return HttpResponse("Hello India")

def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid(): #If the form is valid then save it to the database
            form.save()
            return HttpResponse("Success")

    return render(request, 'index.html', {'form': form})
