from bson import ObjectId
from src.objects.data_objects.DataObject import DataObject
from dataclasses import dataclass


@dataclass
class EmployeeData(DataObject):
    relation_key: ObjectId = None
    data_type = 'employee'


if __name__ == '__main__':
    test = EmployeeData()