from ...extensions.database_extension import db
from ..exceptions.does_not_exist import DoesNotExist


class Repository:
    def __init__(self, entity):
        self.entity = entity
        self.db = db

    def all(self):
        return self.entity.query.all()

    def filter(self, assertion):
        return self.entity.query.filter(assertion)

    def filter_by(self, filters):
        return self.entity.query.filter_by(**filters)

    def filter_all(self, assertion):
        return self.filter(assertion).all()

    def filter_one(self, assertion):
        return self.filter(assertion).one()

    def filter_scalar(self, assertion):
        return self.filter(assertion).scalar()

    def filter_first(self, assertion):
        return self.filter(assertion).first()

    def get(self, identity):
        if instance := self.entity.query.get(identity):
            return instance
        raise DoesNotExist()

    def get_or_404(self, identity):
        return self.filter(self.entity.id == identity).first_or_404()

    def create(self, payload, commit=True):
        instance = self.entity(**payload)

        if commit:
            self.db.session.add(instance)
            self.db.session.commit()

        return instance

    def update(self, identity, payload, commit=True):
        instance = self.get(identity)

        for key, value in payload.items():
            setattr(instance, key, value)

        if commit:
            self.db.session.commit()

        return instance

    def delete(self, identity, commit=True):
        instance = self.get(identity)
        self.db.session.delete(instance)

        if commit:
            self.db.session.commit()

        return instance

    def list(self):
        return self.entity.query.all()

    def list_by(self, filters):
        return self.filter_by(filters).all()
