from Holmes.objects.Obj import Obj
from dataclasses import dataclass


@dataclass
class Company(Obj):
    pass


if __name__ == '__main__':
    c = Company('123')
    c_do = c.create_new_data_object()
    print(c_do)