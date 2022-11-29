from bson import ObjectId
from Holmes.objects.BaseObject import BaseObject
from Holmes.existing.BaseExisting import BaseExisting
from typing import Type
from Holmes import _id


class BaseRelation:
    def __init__(self, obj_1: Type[BaseObject or BaseExisting], obj_2: Type[BaseObject or BaseExisting], source: str,
                 confidence: int):
        """ Relation object used to describe relations between two objects. Please read the parameter description below
        before creating relations.

        :param obj_1: The first object, should be the instigator of the relation. If you for example use a company's name to find employees, the company should be the first object.
        :param obj_2: The object that has a relation with the first object.
        :param source: Source of the relation. Should be the name of the application you've built.
        :param confidence: An integer value of 1 - 100. Data fetched from an official Chamber of Commerce would be 100, while an article would be much lower than that.
        """
        if isinstance(obj_1, BaseObject):
            self.obj_1_data = {
                'instigator': {'_id': obj_1.id.value,
                               'type': obj_1.__class__.__name__}
            }
        else:
            self.obj_1_data = {
                'instigator': obj_1.to_json()
            }

        if isinstance(obj_2, BaseObject):
            self.obj_2_data = {
                'receiver': {'_id': obj_2.id.value,
                             'type': obj_2.__class__.__name__}
            }
        else:
            self.obj_2_data = {
                'receiver': obj_2.to_json()
            }

        self.source = source
        self.confidence = confidence
        self.relation_type = None
        self.relation_id = _id(ObjectId(), 'base')

    def set_relation_type(self, relation_type: str) -> None:
        """
        Sets the optional relation type. If this value is not set, it will also not be included in get_as_dict

        :param relation_type: Relation of type String, for example 'fusion' in case of a business to business relationship.
        :return: None
        """
        self.relation_type = relation_type

    def to_json(self) -> dict:
        relation = {}
        relation.update(self.obj_1_data)
        relation.update(self.obj_2_data)

        self_dict = {
            'source': self.source,
            '_id': self.relation_id.value,
            'confidence': self.confidence,
            'relation': relation
        }

        if self.relation_type is not None:
            self_dict.update({'relation_type': self.relation_type})

        return self_dict

    def __repr__(self):
        return f"{self.to_json()}\n"
