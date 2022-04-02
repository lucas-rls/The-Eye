from email import message
from celery import shared_task
from .models import Category, Event, EventError
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
        error = EventError(message="Category not found", data=request)
        error.save()
        return False
    except Exception as e:
        error = EventError(message=str(e), data=request)
        error.save()
        return False

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
        try:
            error = EventError(message=str(e), data=request)
            error.save()
        except Exception as e:
            print(e)

        return False

    return True