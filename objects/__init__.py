# todo: this isn't very good
from objects import data_objects
from objects.Obj import Obj
from objects.Company import Company
from objects.Domain import Domain
from objects.Place import Place
from objects.Person import Person

data_object_switch = {Person.__name__: data_objects.PersonData,
                      Company.__name__: data_objects.CompanyData,
                      Domain.__name__: data_objects.DomainData,
                      Place.__name__: data_objects.PlaceData}
