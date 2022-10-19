from dataclasses import dataclass
from dataclasses import asdict
from objects.data_objects import exceptions


@dataclass
class DataObject:
    key: str = None
    data: dict = None

    def get_as_dict(self) -> dict:
        """
        Returns this objects attributes in a dictionary.
        Will throw an exception if data or key attributes are empty.

        :return: dict
        """
        if self.data is None:
            raise exceptions.EmptyDataObjectException(self, 'Data not loaded.')
        if self.key is None:
            raise exceptions.EmptyDataObjectException(self, 'Key not loaded.')
        return asdict(self)

    def load_data(self, data: dict) -> None:
        """
        Loads data into your object.

        :param data: Dictionary of your data
        :return: None
        """
        self.data = data


@dataclass
class test(DataObject):
    a: int = None
    b: str = None


if __name__ == '__main__':
    t = test()
    print(t.get_as_dict())