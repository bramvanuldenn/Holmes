from src.objects import Obj
from dataclasses import dataclass


@dataclass
class Domain(Obj):
    ...


if __name__ == '__main__':
    d = Domain('123')
    d.key = '123'
    d.data = {'test_data': 123}
    a = d.create_new_data_object()
    a.data = {1: 1}
    print(d.to_json())