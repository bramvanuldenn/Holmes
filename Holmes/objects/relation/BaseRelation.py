from bson import ObjectId
from Holmes.objects.BaseObject import BaseObject
from typing import Type


class BaseRelation:
    def __init__(self, obj_1: Type[BaseObject], obj_2: Type[BaseObject], source: str, confidence: int):
        """ Relation object used to describe relations between two objects. Please read the parameter description below
        before creating relations.

        :param obj_1: The first object, should be the instigator of the relation. If you for example use a company's name to find employees, the company should be the first object.
        :param obj_2: The object that has a relation with the first object.
        :param source: Source of the relation. Should be the name of the application you've built.
        :param confidence: An integer value of 1 - 100. Data fetched from an official Chamber of Commerce would be 100, while an article would be much lower than that.
        """
        self.obj_1_key = obj_1.key
        self.obj_1_type = obj_1.__class__.__name__

        self.obj_2_key = obj_2.key
        self.obj_2_type = obj_2.__class__.__name__

        self.source = source
        self.confidence = confidence
        self.relation_type = None
        self.relation_key = ObjectId()

    def set_relation_type(self, relation_type: str) -> None:
        """
        Sets the optional relation type. If this value is not set, it will also not be included in get_as_dict

        :param relation_type: Relation of type String, for example 'fusion' in case of a business to business relationship.
        :return: None
        """
        self.relation_type = relation_type

    def get_as_dict(self) -> dict:
        self_dict = {
            'source': self.source,
            # R_ signifies a relationship
            'relation_name': f'R_{self.obj_1_type}_{self.obj_2_type}',
            'relation_key': self.relation_key,
            'confidence': self.confidence,
            'relation':
                {
                    'instigator_key': self.obj_1_key,
                    'instigator_type': self.obj_1_type,

                    'receiver_key': self.obj_2_key,
                    'receiver_type': self.obj_2_type
                }
        }

        if self.relation_type is not None:
            self_dict.update({'relation_type': self.relation_type})

        return self_dict
