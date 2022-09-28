from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SongSerializer
from .models import Song


@api_view(['GET'])
def get_all_songs():

    return Response
