from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
import json


class JSONSchemaValidator(BaseValidator):
    def compare(self, value, schema):
        if not "host" in value:
            raise ValidationError(
                "%(value)s failed JSON schema check", params={"value": value}
            )

        if not "path" in value:
            raise ValidationError(
                "%(value)s failed JSON schema check", params={"value": value}
            )

        try:
            json.loads(value)
        except:
            raise ValidationError(
                "%(value)s failed JSON schema check", params={"value": value}
            )