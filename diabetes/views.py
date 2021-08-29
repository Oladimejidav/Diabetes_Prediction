import pickle

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def diabetes_pre(request):
    template = loader.get_template('index.html')
    Blood Sugar Level Fast = request.POST.get("Blood Sugar Level Fast")
    Blood Sugar Level = request.POST.get("Blood Sugar Level")
    Plasma_R = request.POST.get("Plasma_R")
    Plasma_F = request.POST.get("Plasma_F")
    Hba1c = request.POST.get("Hba1c")
    age = request.POST.get("Age")

    diabetes_data = [
        [  Blood Sugar Level Fast, Blood Sugar Level, Plasma_R, Plasma_F, Hba1c,age]]
    diabetes_model = csv.load(open('diabetes.csv', 'rb'))
    # diabetes_model = pd.read_csv('r',"    diabetes.csv")
    prediction = diabetes.predict(
        [[Blood Sugar Level Fast, Blood Sugar Level, Plasma_R, Plasma_F, Hba1c,age]])
    outcome = prediction


    if outcome == 1:
        result = "Diabetic type 1"
    elif outcome == 2:
        result = "Diabetic Type 2"
     elif outcome == 0:
            result = " Non - Diabetic "


    return HttpResponse(template.render({'result':result}))
