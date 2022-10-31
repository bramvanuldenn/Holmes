from dataclasses import dataclass, asdict
from typing import Union, List
from src.objects import Company, Person, Place, Domain
from datetime import datetime
from src.jobs.Parameters import Parameters
from src.jobs.Parameters import ParamField


@dataclass
class Job:
    applicant_id: str
    contents: List[Union[Company, Person, Place, Domain]]
    parameters: Parameters

    def __post_init__(self):
        self.creation_time = datetime.now()

    def to_json(self) -> dict:
        data = asdict(self)
        data.update({'parameters': data.pop('parameters').to_json()})
        return data


if __name__ == '__main__':
    test = Job('123', [Company('123')], Parameters([ParamField('123', '123', True)]))
    print(test.to_json())