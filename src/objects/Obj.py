from bson import ObjectId
from src.objects.data_objects import DataObject
import src.objects as objects
from dataclasses import dataclass, field, asdict


@dataclass
class Obj:
    key: str
    data: dict = field(default_factory=dict)

    def __post_init__(self):
        self.name = self.__class__.__name__.lower()

    def create_new_data_object(self, key=None) -> DataObject:
        """
        Returns the correct data_object for the class that calls it.
        Also loads the data object with the key of the class that called it.
        If no key is supplied, an ObjectId is generated.

        :return: DataObject(Company, Domain, Person, Place)
        """
        if key is None:
            key = ObjectId()

        args = {
            f'{self.__class__.__name__.lower()}_key': self.key,
            'key': key
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
        # add the name of the object to the dict
        data.update({'object_type': self.__class__.__name__})
        return data


if __name__ == '__main__':
    pass