from bson import ObjectId
from Holmes.data_objects.BaseData import BaseData
from dataclasses import dataclass
from Holmes import _id

@dataclass
class CompanyData(BaseData):
    company_id: _id = None
    data_type = 'company'


@dataclass
class DomainData(BaseData):
    domain_id: _id = None
    data_type = 'domain'


@dataclass
class EmployeeData(BaseData):
    relation_id: _id = None
    data_type = 'employee'


@dataclass
class PersonData(BaseData):
    person_id: _id = None
    data_type = 'person'


@dataclass
class PlaceData(BaseData):
    place_id: _id = None
    data_type = 'place'
