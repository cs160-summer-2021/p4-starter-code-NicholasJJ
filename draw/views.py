# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def bigDisplay(request):
    return render(request, 'draw/bigDisplay.html')

def smallDraw(request):
    return render(request, 'draw/smallDraw.html')

def getGroupInfo(request):
    return render(request, 'draw/getGroupInfo.html')

def wsp(request):
    return render(request, 'draw/1c.html')

def bigGallery(request):
    return render(request, 'draw/bigGallery.html')

def smallTimeUp(request):
    return render(request, 'draw/smallTimeUp.html')
