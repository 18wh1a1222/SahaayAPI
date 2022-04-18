from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from sahaay.models import Users, Needs, Events, Participants, TrackNeeds, Aadhar
from sahaay.serializers import UsersSerializer, NeedsSerializer, ParticipantsSerializer, EventsSerializer, TrackNeedsSerializer, AadharSerializer


@csrf_exempt
def AadharApi(request, aadharId = ""):
    if request.method == 'GET':
        aadhar_details = Aadhar.objects.filter(aadharId=request.GET.get("aadharId"))
        aadhar_serializer = AadharSerializer(aadhar_details, many=True)
        return JsonResponse(aadhar_serializer.data, safe=False)

@csrf_exempt
def LoginApi(request, phno="", password=""):
    if request.method == "POST":
        login_details = JSONParser().parse(request)
        login = Users.objects.filter(phno = login_details["phno"], password= login_details["password"])
        login_serializer = UsersSerializer(login, many=True)
        return JsonResponse(login_serializer.data, safe=False)

@csrf_exempt
def UserApi(request, phno=""):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data = users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully!!!", safe=False)
        return JsonResponse(" Fialed to Add!!!", safe=False)
    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        user = Users.objects.get(phno=users_data["phno"])
        users_serializer = UsersSerializer(user, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully!!!", safe=False)
        return JsonResponse(" Fialed to update!!!", safe=False)

@csrf_exempt
def NeedsApi(request, status="",  needId=0, userId=""):
    if request.method == 'GET':
        if request.GET.get("status") is not None and request.GET.get("needId") is None:
            needs = Needs.objects.filter(status=request.GET.get("status"))
        elif request.GET.get("needId") is not None:
            needs = Needs.objects.filter(needId=request.GET.get("needId"))
        elif request.GET.get("userId") is not None:
            needs = Needs.objects.filter(userId=request.GET.get("userId"))
        else:
            needs = Needs.objects.all()
        needs_serializer = NeedsSerializer(needs, many=True)
        return JsonResponse(needs_serializer.data, safe=False)
    elif request.method == 'POST':
        needs_data = json.loads(request.body)
        user = Users.objects.get(phno=needs_data.get("userId"))
        need = Needs(
            type = needs_data.get("type"),
            desc = needs_data.get("desc"),
            pay = needs_data.get("pay"),
            dop = needs_data.get("dop"),
            doc = needs_data.get("doc"),
            status = needs_data.get("status"),
            userId = user
        )
        need.save()
        return JsonResponse(need)
    elif request.method == 'PUT':
        needs_data = JSONParser().parse(request)
        needs = Needs.objects.get(needId=needs_data["needId"])
        needs_serializer = NeedsSerializer(needs, data=needs_data)
        if needs_serializer.is_valid():
            needs_serializer.save()
            return JsonResponse("Updated Successfully!!!", safe=False)
        return JsonResponse(" Fialed to update!!!", safe=False)

@csrf_exempt
def EventsApi(request, phno=""):
    if request.method == 'GET':
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)
        return JsonResponse(events_serializer.data, safe=False)
    elif request.method == 'POST':
        events_data = JSONParser().parse(request)
        events_serializer = EventsSerializer(data = events_data)
        if events_serializer.is_valid():
            return HttpResponse(events_serializer)
            events_serializer.save()
            return JsonResponse("Added Successfully!!!", safe=False)
        return JsonResponse(" Fialed to Add!!!", safe=False)
    elif request.method == 'PUT':
        events_data = JSONParser().parse(request)
        event = Events.objects.get(phno=events_data["phno"])
        events_serializer = EventsSerializer(event, data=events_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Updated Successfully!!!", safe=False)
        return JsonResponse(" Fialed to update!!!", safe=False)

@csrf_exempt
def EventDetailsApi(request, userId=""):
    if request.method == 'GET':
        events = Participants.objects.filter(userId=request.GET.get("userId"))
        events_serializer = ParticipantsSerializer(events, many=True)
        return JsonResponse(events_serializer.data, safe=False)

