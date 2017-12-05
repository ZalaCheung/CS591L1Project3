from django.http import JsonResponse
from django.shortcuts import render
import dml
import json

# Create your views here.
# @csrf_exempt
# def removeLike(request):
#     try:
#         json_str = ((request.body).decode('utf-8'))
#         body = json.loads(json_str)
#         post = Posts.objects.get(pid=int(body['pid']))
#         user = Users.objects.get(email=body['email'])
#         Likes.objects.filter(pid=post, email=user).delete()
#         return JsonResponse({'result': True})
#     except Exception as e:
#         return JsonResponse({'result': False, 'message': 'error in addLike: ' + str(e)})
#
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def requestResponse(request):
    print("receive request")
    json_str = ((request.body).decode('utf-8'))
    body = json.loads(json_str)
    s = ''
    for rank in body['data']:
        s+=rank
    client = dml.pymongo.MongoClient()
    repo = client.repo
    repo.authenticate('htw93_tscheung_wenjun', 'htw93_tscheung_wenjun')
    BostonHotelPP = repo.htw93_tscheung_wenjun.BostonHotelPotentialPermutation
    hotel = BostonHotelPP.find({'id':s})
    hahahahah = []
    print(hahahahah)
    for h in hotel:
        # print("hotel:" +h)
        hahahahah.append({'cluster':h['cluster']})
    print(hahahahah[0])
    return JsonResponse(hahahahah[0])
    # return JsonResponse({'id':hotel['id'],'lat':hotel['lat'],'long':hotel['long'],'cluster':hotel['cluster']})



