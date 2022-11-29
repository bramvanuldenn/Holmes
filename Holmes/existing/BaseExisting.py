from typing import Tuple
from Holmes.existing import ExistingObjects
from Holmes.existing.Identifier import Identifier


class InvalidIdentifierException(Exception):
    def __init__(self, identifier: Identifier, valid_identifiers: [str]):
        self.identifier = identifier
        self.valid_identifiers = valid_identifiers

    def __str__(self):
        return f"Cannot create ExistingObject with identifier [{self.identifier.identifier_name} " \
               f"-> {self.identifier.identifier_value}]\n Valid identifiers: {self.valid_identifiers}"


class MissingIdentifierException(Exception):
    def __init__(self, identifier_tuple: Tuple[str, ...], identifier_names: [str]):
        self.identifier_tuple = identifier_tuple
        self.identifier_names = identifier_names

    def __str__(self):
        return f"Cannot create ExistingObject with identifiers {self.identifier_names}." \
               f"\nIdentifiers {','.join(self.identifier_tuple)} are mutually inclusive."


class BaseExisting:
    valid_identifier_names = ['SomeRequiredValue', 'OtherRequiredValue', 'Among us']
    object_type = 'base'
    # Identifier names that are in the required_tuples variable are mutually inclusive
    required_tuples = [('SomeRequiredValue', 'OtherRequiredValue')]

    def __init__(self, identifiers: [Identifier]):
        """

        :param identifiers: List of Identifier objects.
        """

        for identifier in identifiers:
            valid = False
            if not self.check_identifier(identifier):

                # This code is here to accept properties that cannot identify on its own, and are only
                # included in required_tuples.
                for req_tuple in self.required_tuples:
                    if identifier.identifier_name in req_tuple:
                        valid = True

                if not valid:
                    raise InvalidIdentifierException(identifier, self.valid_identifier_names)

        # will throw an exception if it doesnt work
        self.check_identifier_tuples(identifiers)
        self.identifiers = identifiers

    def check_identifier(self, identifier: Identifier) -> bool:
        return identifier.identifier_name in self.valid_identifier_names

    def check_identifier_tuples(self, identifiers: [Identifier]) -> bool:
        # Fetching all identifiers' names
        base_identifiers = [i.identifier_name for i in identifiers]
        identifier_names = [i.identifier_name for i in identifiers]
        # Looping through all identifiers that are mutually inclusive
        for required_tuple in self.required_tuples:

            # Checking how many identifier names match with the mutually inclusive identifiers
            found = [identifier for identifier in identifier_names if identifier in required_tuple]

            # (house_number, street_name) and (house_number, postal_code) shouldn't throw an exception
            # if the former matches, but the latter lacks a postal_code. Hence why we remove used identifier_names.
            identifier_names = [name for name in identifier_names if name not in found]

            # If none of the mutually inclusive identifiers were found, or all of them, that means the object is OK.
            # if not, we raise an exception.
            if len(found) != len(required_tuple) and len(found) != 0:
                raise MissingIdentifierException(required_tuple, base_identifiers)

        return True

    def to_json(self) -> dict:
        identifiers = {i.identifier_name: i.identifier_value for i in self.identifiers}
        return {
            'type': self.object_type,
            'identifiers': identifiers
        }


if __name__ == '__main__':
    be = BaseExisting([Identifier('SomeRequiredValue', 123),
                       Identifier('Among us', 123)])
    print(be.to_json())