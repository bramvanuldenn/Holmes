from dataclasses import dataclass
from dataclasses import asdict
from typing import Any

"""Params are formatted like this:
    [
        {'param_name': 'param1', 'param_type': 'int', 'required_field': True}, 
        {'param_name': 'param2', 'param_type': 'str', 'required_field': False}
    ]

"""


@dataclass
class ParamField:
    field_name: str
    field_type: str
    required_field: bool = True
    value: Any = None


class Parameters:
    def __init__(self, param_fields: [ParamField] = None):
        if param_fields:
            self.fields = param_fields
        else:
            self.fields = []

    def get_field(self, field_name: str) -> ParamField:
        for f in self.fields:
            if f.field_name == field_name:
                return f

    def load_parameter(self, parameter: ParamField) -> None:
        self.fields.append(parameter)

    def load_parameters(self, parameters: [ParamField]) -> None:
        [self.fields.append(parameter) for parameter in parameters]

    def from_json(self, parameters_json: [dict]) -> None:
        for parameter_dict in parameters_json:
            field_name = parameter_dict.get('field_name')
            field_type = parameter_dict.get('field_type')
            required_field = parameter_dict.get('required_field')
            self.fields.append(ParamField(field_name, field_type, required_field=required_field))

    def to_json(self) -> [dict]:
        data = []
        for f in self.fields:
            data.append(asdict(f))
        return data


if __name__ == '__main__':
    p = Parameters()
    p.from_json([
        {'field_name': 'param1', 'field_type': 'int', 'required_field': True},
        {'field_name': 'param2', 'field_type': 'str', 'required_field': False}
    ])
    field = p.get_field('param1')
    print(p.to_json())
