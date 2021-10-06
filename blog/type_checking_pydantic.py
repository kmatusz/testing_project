# Type annotation:
class Coffee():
    def __init__(self, name: str) -> None:
        self.name = name
    
    def get_name(self) -> str:
        return self.name


def create_coffee(name) -> Coffee:
    return Coffee(name)

a = create_coffee('Java')
print(a.get_name())

# using pydantic
from pydantic import BaseModel, EmailStr # all classes that need validation should be inherited from basemodel
from pydantic.class_validators import validator
from typing import List, Optional

class Roastery(BaseModel):
    # Specify the fields of the class
    name: str 
    email: EmailStr # special email validator
    year_funded: int # if passed name is '1997' it will be converted to int
    coffees: List[str] # if passed is str then it will not be converted
    motto: Optional[str] # optional

    # custom validator - first specify fields of the class
    # always - whether check if the field is optional
    # pre - whather check before the field is converted to correct type or after
    @validator('year_funded', always=True, pre=False)
    def is_valid_year(cls, v):
        if not 1800 < v < 2100:
            raise ValueError(
                'Wrong year'
            )
        return v

    def __str__(self) -> str:
        return f"{self.name}: Funded in {self.year_funded}, Email: {self.email}"


nomad = Roastery(name='Nomad', email = 'nomad@coffee.com', year_funded = '1997', coffees = ['Filter'])
nomad2 = Roastery(name='Nomad', email = 'nomad@coffee.com', year_funded = '1997', coffees = ['Filter'], motto='aaa')
print(nomad)
print(type(nomad.year_funded))


