from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .tasks import save_event
import json


@require_POST
@csrf_exempt
def collector(request):
    task = save_event.delay(json.loads(str(request.body.decode("utf-8"))))
    return JsonResponse({"task": str(task)})