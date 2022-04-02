from celery import shared_task
from .models import Category, Event
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from http import HTTPStatus
import time


@shared_task()
def save_event(request):
    category_name = request.get("category")

    try:
        category = Category.objects.get(name=category_name)
    except ObjectDoesNotExist:
        return {"msg": "Something went wrong"}
    except:
        return {"msg": "Something went wrong"}

    try:
        event = Event(
            session_id=request.get("session_id"),
            category=category,
            name=request.get("name"),
            data=request.get("data"),
            timestamp=request.get("timestamp"),
        )

        event.save()
    except Exception as e:
        return {"msg": "Something went wrong"}

    time.sleep(20)