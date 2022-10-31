from bson import ObjectId
from Holmes.data_objects.DataObject import DataObject
from dataclasses import dataclass


@dataclass
class CompanyData(DataObject):
    data_type = 'company'


if __name__ == '__main__':
    t = CompanyData(ObjectId(), {})
    print(t.to_json())