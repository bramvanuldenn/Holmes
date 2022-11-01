from Holmes.objects.relation.BaseRelation import BaseRelation
from Holmes.objects.Objects import Company, Person


class InvalidEmployeeException(Exception):
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def __str__(self):
        return f"Unable to form an Employee object with objects {self.obj1} and {self.obj2} \n" \
               f"The first object should be a Company, the second should be a Person."


class Employee(BaseRelation):
    def __init__(self, obj_1: Company, obj_2: Person, source: str, confidence: int) -> None:
        """ Relation object used to describe relations between two objects. Please read the parameter description below
                before creating relations. Will throw an exception if obj_1 and obj_2 are not a company and person respectively.

                :param obj_1: Company object
                :param obj_2: Person object
                :param source: Source of the relation. Should be the name of the application you've built.
                :param confidence: An integer value of 1 - 100. Data fetched from an official Chamber of Commerce would be 100, while an article would be much lower than that.
                """
        if not isinstance(obj_1, Company) or not isinstance(obj_2, Person):
            raise InvalidEmployeeException(obj_1, obj_2)
        super().__init__(obj_1, obj_2, source, confidence)

    def get_as_dict(self) -> dict:
        """Same as a standard Relation object, except the relation_name is overwritten with 'employee' """
        data = super().get_as_dict()
        data.update({'relation_name': 'employee'})
        return data


if __name__ == '__main__':
    t = Employee(Company('the new standard'), Person('chiel'), 'somewhere', 100)
    print(t.get_as_dict())

