from ....common.exceptions.does_not_exist import DoesNotExist
from ....common.utils.repository import Repository
from ....entities import Expense


class ExpenseRepository(Repository):
    def get_all_expenses_from_profile(self, profile_id: int):
        return self.filter_by({"profile_id": profile_id}).all()

    def get_expense(self, id: int, profile_id: int):
        return self.filter_by({"id": id, "profile_id": profile_id}).one()

    def update(self, identity, payload, commit=True):
        instance = self.get_expense(identity, payload["profile_id"])

        for key, value in payload.items():
            setattr(instance, key, value)

        if commit:
            self.db.session.commit()

        return instance

    def delete(self, identity: int, profile_id: int, commit=True):
        instance = self.get(identity)

        if instance.profile_id != profile_id:
            raise DoesNotExist()

        self.db.session.delete(instance)

        if commit:
            self.db.session.commit()

        return instance


expense_repository = ExpenseRepository(Expense)
