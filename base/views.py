from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
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






