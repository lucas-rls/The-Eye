from unicodedata import name
from django.shortcuts import render
from datetime import datetime
import requests
import json


def home(request):
    if request.method == "POST":
        event = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "banner image click",
            "data": {
                "host": "www.website.com",
                "path": "/",
            },
            "timestamp": str(datetime.now()),
        }

        requests.post(
            "http://127.0.0.1:8000/collector/",
            headers={"content-type": "application/json"},
            data=json.dumps(event),
        )

        return render(request, "index.html")
    else:
        event = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {"host": "www.website.com", "path": "/"},
            "timestamp": str(datetime.now()),
        }

        requests.post(
            "http://127.0.0.1:8000/collector/",
            headers={"content-type": "application/json"},
            data=json.dumps(event),
        )

        return render(request, "index.html")


def form(request):
    if request.method == "POST":
        event = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "form interaction",
            "name": "submit",
            "data": {
                "host": "www.website.com",
                "path": "/form",
                "form": {
                    "name": request.POST.get("name"),
                    "email": request.POST.get("email"),
                },
            },
            "timestamp": str(datetime.now()),
        }

        requests.post(
            "http://127.0.0.1:8000/collector/",
            headers={"content-type": "application/json"},
            data=json.dumps(event),
        )

        return render(request, "form.html")
    else:
        event = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {"host": "www.website.com", "path": "/form"},
            "timestamp": str(datetime.now()),
        }

        requests.post(
            "http://127.0.0.1:8000/collector/",
            headers={"content-type": "application/json"},
            data=json.dumps(event),
        )
        return render(request, "form.html")
