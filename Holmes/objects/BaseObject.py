from typing import Type

from bson import ObjectId
from Holmes.data_objects import BaseData
import Holmes.objects as objects
from dataclasses import dataclass, field, asdict
from datetime import datetime
from Holmes import _id

@dataclass
class BaseObject:
    _id: _id
    data: dict = field(default_factory=dict)

    def __post_init__(self):
        if self._id is None:
            self._id = _id(ObjectId(), 'base')
        self.name = self.__class__.__name__.lower()

    def create_new_data_object(self, key=None) -> BaseData:
        """
        Returns the correct data_object for the class that calls it.
        Also loads the data object with the key of the class that called it.
        If no key is supplied, an ObjectId is generated.

        :return: DataObject(Company, Domain, Person, Place)
        """
        if key is None:
            key = ObjectId()

        args = {
            f'{self.__class__.__name__.lower()}_id': self.key,
        }
        return objects.data_object_switch.get(self.__class__.__name__)(**args)

    def load_data(self, data: dict) -> None:
        """
        Loads dictionary data into the object. Typically, this data is used as input or parameters inside of
        scraping applications.

        :param data: dictionary data about the object
        :return: None
        """
        self.data.update(data)

    def to_json(self) -> dict:
        data = asdict(self)
        # data property is used for generating new data using it - the property itself does never hold any new data.
        # hence why it is deleted.
        data.pop('data')

        data['_id'] = data.pop('key')
        # add the name of the object to the dict
        data.update({'type': self.__class__.__name__})
        data['creation_timestamp'] = datetime.now()

        return data

    @property
    def id(self):
        return self._id


if __name__ == '__main__':
    pass