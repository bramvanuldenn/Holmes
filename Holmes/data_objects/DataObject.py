from dataclasses import dataclass, asdict, field
from bson import ObjectId
from Holmes.data_objects import exceptions


@dataclass
class DataObject:
    key: ObjectId
    data: dict = field(default_factory=dict)
    data_type = 'base_type'

    def to_json(self) -> dict:
        """
        Returns this objects attributes in a dictionary.
        Will throw an exception if data or key attributes are empty.

        :return: dict
        """
        if self.data is None:
            raise exceptions.EmptyDataObjectException(self, 'Data not loaded.')
        if self.key is None:
            raise exceptions.EmptyDataObjectException(self, 'Key not loaded.')

        self_dict = asdict(self)
        self_dict.update({'data_type': self.data_type})

        return self_dict

    def load_data(self, data: dict) -> None:
        """
        Loads data into your object.

        :param data: Dictionary of your data
        :return: None
        """
        self.data.update(data)


@dataclass
class test(DataObject):
    a: int = None
    b: str = None


if __name__ == '__main__':
    t = DataObject(ObjectId())
    print(t.to_json())