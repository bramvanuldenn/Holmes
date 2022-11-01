from bson import ObjectId
from Holmes.data_objects.BaseData import BaseData
from dataclasses import dataclass


@dataclass
class CompanyData(BaseData):
    data_type = 'company'


@dataclass
class DomainData(BaseData):
    data_type = 'domain'


@dataclass
class EmployeeData(BaseData):
    relation_key: ObjectId = None
    data_type = 'employee'


@dataclass
class PersonData(BaseData):
    data_type = 'person'


@dataclass
class PlaceData(BaseData):
    data_type = 'place'
