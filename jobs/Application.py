from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Application:
    applicant_id: str
    applicant_name: str
    amount: int
    parameters: dataclass = None

    def __post_init__(self):
        self.creation_time = datetime.now()
