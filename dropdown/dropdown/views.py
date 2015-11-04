from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dropdown.forms import DropDownForm
from dropdown.models import Country, State, City
import json


def dropdown(request):
    form = DropDownForm()
    return render(request, "dropdown.html", {'form':form})

    """ 'Without using ModelForm'

    country = Country.objects.all()
    state = State.objects.all()
    city = City.objects.none()
    return render(request, "dropdown.html", {'country': country, 'state':state, 'city':city})
 
    """


def state_ajax(request):
    if request.POST and request.is_ajax():
        print "ajax"
        c_id = request.POST.get('country_id')
        print id
        state = State.objects.filter(country=c_id)
	print state
        state_dict = {}
        for state in state:
            state_dict[state.id] = state.name
	print state_dict, json.dumps(state_dict)
        return JsonResponse(state_dict, content_type="application/json") #shortcut for json.dumps

def city_ajax(request):
    if request.POST and request.is_ajax():
        s_id = request.POST.get('state_id')
	print s_id
        city = City.objects.filter(state=s_id)
	print city
        city_dict = {}
        for city in city:
            city_dict[city.id] = city.name
        return HttpResponse(json.dumps(city_dict), content_type="application/json")  
