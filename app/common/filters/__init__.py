from json import loads

from ..utils.repository import Repository


class Filters:
    operators = {
        "lte": lambda attribute, value: attribute <= value,
        "lt": lambda attribute, value: attribute < value,
        "gte": lambda attribute, value: attribute >= value,
        "gt": lambda attribute, value: attribute > value,
        "eq": lambda attribute, value: attribute == value,
        "df": lambda attribute, value: attribute != value,
        "in": lambda attribute, value: attribute.in_(loads(value)),
    }

    def __init__(self, repository):
        self.repository: Repository = repository

    def execute(self, filters):
        parsed_filters = self.parse_filters(filters)
        filter_list = []

        for filter_key in parsed_filters.keys():
            try:
                assertion, is_ok = self.handle_filter(filter_key, parsed_filters)
                if is_ok:
                    filter_list.append(assertion)

            except ValueError:
                continue

        return self.repository.filter_list(*filter_list)

    def handle_filter(self, filter_key, filters):
        attribute, operator = self.parse_key(filter_key)
        value = filters[filter_key]
        filter_fn = self.operators.get(operator, None)

        if filter_fn and attribute:
            return filter_fn(attribute, value), True

        return None, False

    def parse_filters(self, filters):
        return dict(filters)

    def parse_key(self, key):
        field_name, operator = key.split("__")
        return self.repository.get_entity_attribute(field_name), operator
