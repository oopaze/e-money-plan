from app.entities import Profile
from marshmallow_sqlalchemy.schema import SQLAlchemyAutoSchema


class ShowProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        fields = ("id", "email", "salary", "created_at", "updated_at")
