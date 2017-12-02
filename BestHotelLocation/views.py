from django.http import JsonResponse
from django.shortcuts import render
import dml

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
    client = dml.pymongo.MongoClient()
    repo = client.repo
    repo.authenticate('htw93_tscheung_wenjun', 'htw93_tscheung_wenjun')
    BostonHotelCustomScore = repo.htw93_tscheung_wenjun.BostonHotelCustomScore
    BostonHotel = repo.htw93_tscheung_wenjun.BostonHotel
    hotel = BostonHotel.find()
    flag = False
    for h in hotel:
        if h['Hotel_name'] =='Boston Harbor Hotel':
            flag = True
    return JsonResponse({'a':flag})




