import json
import mechanize

from django.shortcuts import redirect
from django.conf import settings

from classroom.models import Classroom, Building


def astra_connect(request):
    br = mechanize.Browser()
    br.open("https://classrooms.rice.edu/astraProd/Logon.aspx?nosso=")
    br.select_form(name="aspnetForm")
    br["ctl00$MainContentPlaceHolder$MainLogin$UserName"] = settings.ASTRA_USER
    br["ctl00$MainContentPlaceHolder$MainLogin$Password"] = settings.ASTRA_PASS
    br.submit()

    return br


def update_buildings(request):
    br = astra_connect(request)
    building_response = br.open("https://classrooms.rice.edu/AstraProd/~api/entity/building")
    building_data = json.loads(building_response.read())

    records = building_data['totalRecords']
    i = 0
    while i < records:
        astra_id = building_data['data'][i]['Id']
        code = building_data['data'][i]['BuildingCode']
        description = building_data['data'][i]['Description']
        Building.objects.get_or_create(astra_id=astra_id, code=code, name=description)
        i = i + 1

    return redirect('/admin/astra/building/')


def all_classrooms_update(request):
    br = astra_connect(request)
    classroom_response = br.open("https://classrooms.rice.edu/AstraProd/~api/query/room?fields=Id,Name,RoomNumber,MaxOccupancy,ModifiedDate,BuildingId")
    classroom_data = json.loads(classroom_response.read())

    records = classroom_data['totalRecords']
    i = 0
    while i < records:
        print classroom_data['data']
        astra_id = classroom_data['data'][i][0]
        name = classroom_data['data'][i][1]
        room_number = classroom_data['data'][i][2]
        seats = classroom_data['data'][i][3]
        modified = classroom_data['data'][i][4]
        building_id = classroom_data['data'][i][5]
        building = Building.objects.get(astra_id=building_id)
        Classroom.objects.get_or_create(seats=seats, room_number=room_number, building=building)
        i = i + 1

    return redirect('/admin/astra/classroom/')