from flask_marshmallow.fields import fields
from marshmallow import ValidationError

from ..utils.enum import Enum


class Enum(fields.String):
    default_error_messages = {"required": "Campo é obrigatório"}

    def __init__(self, *args, enum: Enum, **kwargs):
        self.enum = enum
        validations = kwargs.get("validate", [])
        validations.append(self.is_valid)

        kwargs["validate"] = validations
        super().__init__(*args, **kwargs)

    def serialize(self, attr, obj, *args, **kwargs):
        enum_option = getattr(obj, attr)
        if enum_option is None:
            return None

        return enum_option.value

    def is_valid(self, value):
        if not self.enum.has_value(value):
            raise ValidationError(f"{value} não é uma opção válida")
