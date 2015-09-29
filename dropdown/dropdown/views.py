from django.shortcuts import render
from django.http import HttpResponse
from dropdown.forms import DropDownForm
from dropdown.models import Country, State, City
import json

def dropdown(request):
    #form = DropDownForm()
    c = Country.objects.all()
    s = State.objects.all()
    ci = City.objects.none()
    return render(request, "dropdown.html", {'c': c, 's':s, 'ci':ci})


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
	print json.dumps(state_dict)
    	return HttpResponse(json.dumps(state_dict), content_type="application/json")

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
