from django.http import JsonResponse
from django.shortcuts import render

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

    return JsonResponse({})




