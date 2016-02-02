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
        state = State.objects.filter(country=c_id)

        for s in state:
            city = s.city_set.all()
            print "city", city


        state_dict = {}
        for s in state:
            state_dict[s.id] = s.name
        
        city_dict = {}
        print city
        for c in city:
            city_dict[c.id] = c.name


        data = json.dumps({
                'state_dict': state_dict,
                'city_dict': city_dict,
            })

        print data
        return HttpResponse(data, content_type="application/json")