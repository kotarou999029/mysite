from django.shortcuts import render
from .models import Health
from .forms import helthForm

def index(request):
    return render(request, 'index.html')

def chart(request):
    Health_list = Health.objects.filter(staff_no=21850)
    return render(request, 'chart.html', {'Health_list': Health_list})

def nyuryoku(request):
    form = helthForm()
    

    if request.method == 'POST':
        form = helthForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    context = {'form': form}
    return render(request, 'nyuryoku.html', context)