from django.test import TestCase
from .models import Event, Category
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.utils import IntegrityError
from django.urls import reverse
from http import HTTPStatus
import json


class CollectorTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="page interaction")
        self.category = Category.objects.all()[0]

        self.event = Event(
            session_id="e2085be2-9137-4e4e-80b5-f1ffddc25420",
            category=self.category,
            name="pageview",
            data="""{
                "host": "www.consumeraffairs.com",
                "path": "/",
            }""",
            timestamp="2021-02-01 09:15:27.243860",
        )
        self.event.save()

    def test_inexistent_category(self):
        with self.assertRaises(ObjectDoesNotExist):
            Category.objects.get(name="inexistent_category")

    def test_invalid_timestamp(self):
        with self.assertRaises(ValidationError):
            event = Event(
                session_id="e2085be2-9137-4e4e-80b5-f1ffddc25423",
                category=self.category,
                name="pageview",
                data="""{
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                }""",
                timestamp="2021-01-017 09:15:27.243860",
            )
            event.full_clean()

    def test_invalid_data_json(self):
        with self.assertRaises(ValidationError):
            event = Event(
                session_id="e2085be2-9137-4e4e-80b5-f1ffddc25423",
                category=self.category,
                name="pageview",
                data="""{
                    "path": "/",
                }""",
                timestamp="2021-01-01 09:15:27.243860",
            )
            event.full_clean()

    def test_missing_session_id(self):
        with self.assertRaises(ValidationError):
            event = Event(
                category=self.category,
                name="pageview",
                data="""{
                    "path": "/",
                }""",
                timestamp="2021-01-01 09:15:27.243860",
            )
            event.full_clean()

    def test_missing_category_id(self):
        with self.assertRaises(ValidationError):
            event = Event(
                session_id="e2085be2-9137-4e4e-80b5-f1ffddc25423",
                name="pageview",
                data="""{
                    "path": "/",
                }""",
                timestamp="2021-01-01 09:15:27.243860",
            )
            event.full_clean()

    def test_missing_name(self):
        with self.assertRaises(ValidationError):
            event = Event(
                session_id="e2085be2-9137-4e4e-80b5-f1ffddc25423",
                category=self.category,
                data="""{
                    "path": "/",
                }""",
                timestamp="2021-01-01 09:15:27.243860",
            )
            event.full_clean()

    def test_missing_timestamp(self):
        with self.assertRaises(ValidationError):
            event = Event(
                session_id="e2085be2-9137-4e4e-80b5-f1ffddc25423",
                category=self.category,
                name="pageview",
                data="""{
                    "path": "/",
                }""",
            )
            event.full_clean()

    def test_unique_violation(self):
        with self.assertRaises(IntegrityError):
            event = Event(
                session_id="e2085be2-9137-4e4e-80b5-f1ffddc25420",
                category=self.category,
                name="pageview",
                data="""{
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                }""",
                timestamp="2021-02-01 09:15:27.243860",
            )
            event.save()

    def test_post_request(self):
        data = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "cta click",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "element": "chat bubble",
            },
            "timestamp": "2021-01-01 09:15:27.243860",
        }

        response = self.client.post(
            reverse("collector"), data, content_type="application/json"
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)