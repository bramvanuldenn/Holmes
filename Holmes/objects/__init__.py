# todo: this isn't very good
from Holmes import data_objects
from Holmes.objects.Obj import Obj
from Holmes.objects.Company import Company
from Holmes.objects.Domain import Domain
from Holmes.objects.Place import Place
from Holmes.objects.Person import Person
from typing import Type, Union
from enum import Enum
from bson import ObjectId


class UnknownObjectNameException(Exception):
    def __init__(self, object_name: str):
        self.object_name = object_name

    def __str__(self):
        return f"Object name {self.object_name} is unknown. Use company, person, place or domain."


data_object_switch = {Person.__name__: data_objects.PersonData,
                      Company.__name__: data_objects.CompanyData,
                      Domain.__name__: data_objects.DomainData,
                      Place.__name__: data_objects.PlaceData}


class ObjectsEnum(Enum):
    COMPANY = Company
    PERSON = Person
    DOMAIN = Domain
    PLACE = Place


def create_object(object_type: ObjectsEnum, key=None, object_data=None) -> Type[Obj]:
    """
    Creates any of the 4 object types.

    :param object_data: Optional dictionary to fill your object with.
    :param object_type: Objects class Enum, options are COMPANY, PERSON, DOMAIN or PLACE.
    :param key: An UUID4 key, if none is supplied this function will generate it.
    :return: A company, domain, person or place object.
    """
    if key is None:
        key = ObjectId()
    args = {'key': key}

    if object_data is not None:
        args.update({'data': object_data})

    return object_type.value(**args)


def from_json(json_data: dict) -> Union[Company, Place, Person, Domain]:
    object_type = json_data.pop('object_type')

    if object_type == 'Company':
        return ObjectsEnum.COMPANY.value(**json_data)
    if object_type == 'Person':
        return ObjectsEnum.PERSON.value(**json_data)
    if object_type == 'Place':
        return ObjectsEnum.PLACE.value(**json_data)
    if object_type == 'Domain':
        return ObjectsEnum.DOMAIN.value(**json_data)

    raise UnknownObjectNameException(object_type)


if __name__ == '__main__':
    obj = from_json({'key': '123', 'data': {'test_data': 123}, 'object_type': 'Domain'})
    data = obj.to_json()
    new_obj = from_json(data)
    print(f"old: {data}\nnew: {new_obj.to_json()}\ncompared: {data == new_obj.to_json()}")
