from json import JSONDecodeError

from flask_jwt_extended import get_jwt_identity

from ....common.filters import Filters
from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase


class ListExpensiesUseCase(UseCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_handler = Filters(self.repository)

    def execute(self, payload=None, id=None, filters=None):
        instances = self._handle_filters(filters)
        dumped_instances = self.output_schema.dump(instances, many=True)
        return success_response(dumped_instances, "expensies")

    def _handle_filters(self, filters):
        try:
            return self.filter_handler.execute(filters)
        except (JSONDecodeError, TypeError) as e:
            print(e)
            return self.repository.get_all_expenses_from_profile(get_jwt_identity())
