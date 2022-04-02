from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Event
from django.core.exceptions import ObjectDoesNotExist
from http import HTTPStatus
import json


@csrf_exempt
@require_POST
def collector(request):
    category_name = request.POST.get("category")

    try:
        category = Category.objects.get(name=category_name)
    except ObjectDoesNotExist:
        return JsonResponse(
            {"msg": "Category does not exist"}, status=HTTPStatus.BAD_REQUEST
        )
    except:
        return JsonResponse(
            {"msg": "Something went wrong"}, status=HTTPStatus.INTERNAL_SERVER_ERROR
        )

    try:
        event = Event(
            session_id=request.POST.get("session_id"),
            category=category,
            name=request.POST.get("name"),
            data=request.POST.get("data"),
            timestamp=request.POST.get("timestamp"),
        )

        event.save()
    except Exception as e:
        return JsonResponse({"msg": str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

    return JsonResponse(request.POST)