from flask import request
from flask_marshmallow.fields import fields
from marshmallow import ValidationError, validate


class Email(fields.String):
    default_error_messages = {
        "required": "Email é um campo obrigatório",
    }

    def __init__(self, *args, repository, **kwargs):
        self.repository = repository
        self.validations = kwargs.get("validate", [])
        self.validations.append(validate.Email(error="Email inválido"))
        self.validations.append(self.is_unique)

        kwargs.update({"validate": self.validations})
        super().__init__(*args, **kwargs)

    def is_unique(self, email):
        instance_id = request.view_args.get("id", 0)
        if not self.repository.check_email_is_unique(email, instance_id):
            raise ValidationError("Email já está em uso")
