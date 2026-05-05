from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json
from .models import RoomMember
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def getToken(request):
    #Build token with uid
    appId = 'b7f67d03d0ce449e9970fc8e97cb6074'
    appCertificate = 'b241652d33e04c96bec3a7b347aa6e67'
    channelName = request.GET.get('channel').upper()
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600*24
    currentTimeStapms = int(time.time()) # Tam sayıya çevirmek daha garantidir
    privilegeExpiredTs = currentTimeStapms + expirationTimeInSeconds
    role = 1 # 1 is host 2 is guess

    # token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, int(uid), role, privilegeExpiredTs)

    print(f"Token Üretiliyor: Kanal={channelName}, UID={uid}, AppID={appId}")
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, int(uid), role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid}, safe=False)



def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name = data['name'],
        uid = data['uid'],
        room_name =data['room_name']
    )
    return JsonResponse({'name':data['name']}, safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid = uid,
        room_name = room_name,
    )
    name = member.name
    return JsonResponse({'name':name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)

    member = RoomMember.objects.get(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name'],
    )
    member.delete()
    return JsonResponse('Member was deleted', safe=False)
