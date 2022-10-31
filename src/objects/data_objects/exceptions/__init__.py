class EmptyDataObjectException(Exception):
    def __init__(self, data_object, missing_data: str):
        self.data_object = data_object
        self.missing_data = missing_data

    def __str__(self):
        return f"{self.data_object.__class__.__name__} is missing data: {self.missing_data}"
