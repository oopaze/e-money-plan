class DoesNotExist(Exception):
    message = "Identifier does not chocks with any instance"

    def __init__(self, message=message) -> None:
        super().__init__(message)
