from flask_marshmallow.fields import fields
from marshmallow import ValidationError


class Money(fields.Decimal):
    default_error_messages = {"required": "Este campo é obrigatório"}

    def __init__(self, *args, **kwargs):
        validations = kwargs.get("validate", [])
        validations.append(self.validate_is_positive)

        kwargs["validate"] = validations
        super().__init__(*args, **kwargs)

    def validate_is_positive(self, value):
        if value < 0:
            raise ValidationError("O valor deve ser 0 ou maior")
