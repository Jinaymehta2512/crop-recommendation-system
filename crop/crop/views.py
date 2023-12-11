from django.http import HttpResponse
from django.shortcuts import render
import joblib 
def home(request):
    cls = joblib.load('crop_pred.sav')

    lis = []

    lis.append(request.GET['Nitrogen'])
    lis.append(request.GET['Phosphorus'])
    lis.append(request.GET['Potassium'])
    lis.append(request.GET['Temperature'])
    lis.append(request.GET['Humidity'])
    lis.append(request.GET['Rainfall'])
    lis.append(request.GET['pH'])

    ans = cls.predict([lis])



    return render(request,'home.html',{'ans':ans})

