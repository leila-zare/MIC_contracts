from django.shortcuts import render
from django.shortcuts import HttpResponse
from jalali_date import datetime2jalali, date2jalali

def about(request):
    # return HttpResponse('hi there! Im hello World!')
    return render(request , 'about.html')

def Home(request):
    # return HttpResponse('Home')
    return render(request, 'Home.html')

def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')