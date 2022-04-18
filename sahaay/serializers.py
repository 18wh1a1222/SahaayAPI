from django.db import models
from rest_framework import serializers
from sahaay.models import Users, Needs, Events, Participants, TrackNeeds, Aadhar

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        depth = 1

class NeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = '__all__'
        depth = 1

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        depth = 1

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'
        depth = 1

class TrackNeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackNeeds
        fields = '__all__'
        depth = 1

class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = '__all__'
        depth = 1
