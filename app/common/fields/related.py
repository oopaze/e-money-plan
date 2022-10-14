from marshmallow import ValidationError
from marshmallow.fields import Field

from ..exceptions.does_not_exist import DoesNotExist


class Related(Field):
    default_error_messages = {"required": "Campo obrigatório"}

    def __init__(self, *args, repository, field=None, **kwargs):
        self.field = field

        validations = kwargs.get("validate", [])
        validations.append(self.validate_exists)

        kwargs["validate"] = validations
        super().__init__(*args, **kwargs)

        self.repository = repository

    def validate_exists(self, value):
        if self.field is not None:
            return self.validate_by_field(value)
        return self.validate_by_id(value)

    def validate_by_field(self, value):
        field = getattr(self.repository.entity, self.field)

        if not any(self.repository.filter_all(field == value)):
            raise ValidationError(f"{self.field} {value} does not exists")

    def validate_by_id(self, value):
        try:
            self.repository.get(value)
        except DoesNotExist:
            raise ValidationError(f"ID {value} does not exists")
