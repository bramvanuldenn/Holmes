from data_objects import DataObject
import objects
from dataclasses import dataclass


@dataclass
class Obj:
    key: str
    data: dict = None

    def create_new_data_object(self) -> DataObject:
        """
        Returns the correct data_object for the class that calls it.
        Also loads the data object with the key of the class that called it.

        :return: DataObject(Company, Domain, Person, Place)
        """
        return objects.data_object_switch.get(self.__class__.__name__)(key=self.key)

    def load_data(self, data: dict) -> None:
        """
        Loads dictionary data into the object. Typically, this data is used as input or parameters inside of
        scraping applications.

        :param data: dictionary data about the object
        :return: None
        """