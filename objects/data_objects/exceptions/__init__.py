class EmptyDataObjectException(Exception):
    def __init__(self, data_object, what: str):
        self.data_object = data_object

        self.what = what

    def __str__(self):
        return f"{self.data_object.__class__.__name__} is missing data: {self.what}"
