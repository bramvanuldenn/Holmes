from dataclasses import dataclass, asdict, field
from Holmes import _id
from Holmes.data_objects import exceptions
from datetime import datetime


@dataclass
class BaseData:
    _id: _id
    parent_id: _id
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
        if self._id is None:
            raise exceptions.EmptyDataObjectException(self, 'Key not loaded.')

        self_dict = asdict(self)

        self_dict.update(self_dict.pop('data'))
        self_dict.update({'data_type': self.data_type})

        # Extracting value from _id object
        self_dict['_id'] = self._id.value
        self_dict['parent_id'] = self.parent_id.value
        self_dict['creation_timestamp'] = datetime.now()
        return self_dict

    def load_data(self, data: dict) -> None:
        """
        Loads data into your object.

        :param data: Dictionary of your data
        :return: None
        """
        self.data.update(data)

    @property
    def id(self) -> _id:
        return self._id


@dataclass
class test(BaseData):
    a: int = None
    b: str = None


if __name__ == '__main__':
    t = BaseData(ObjectId())
    print(t.to_json())