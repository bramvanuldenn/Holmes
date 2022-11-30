from dataclasses import dataclass
from bson import ObjectId


@dataclass
class _id:
    value: ObjectId
    name: str

