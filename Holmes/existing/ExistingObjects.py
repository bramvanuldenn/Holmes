from Holmes.existing.BaseExisting import BaseExisting


class ExistingCompany(BaseExisting):
    object_type = 'ExistingCompany'
    valid_identifier_names = ['company_identifier', 'company_key']
    required_tuples = [('company_identifier', 'country_code')]


class ExistingPerson(BaseExisting):
    object_type = 'ExistingPerson'
    valid_identifier_names = ['person_key']
    required_tuples = []


class ExistingDomain(BaseExisting):
    object_type = 'ExistingDomain'
    valid_identifier_names = ['domain_name', 'top_level_domain', 'domain_key']
    required_tuples = [('domain_name', 'top_level_domain')]


class ExistingPlace(BaseExisting):
    object_type = 'ExistingPlace'
    valid_identifier_names = ['place_key', 'street_name', 'postal_code', 'house_number']
    required_tuples = [('street_name', 'house_number'), ('postal_code', 'house_number')]


class ExistingEmployee(BaseExisting):
    object_type = 'ExistingEmployee'
    valid_identifier_names = ['employee_key']
    required_tuples = []


if __name__ == '__main__':
    from Holmes.existing.Identifier import Identifier
    c = ExistingCompany([Identifier('country_code', 'NL')])