from pydantic import BaseModel
from pydantic import validator
from pydantic import EmailStr
from pydantic import constr


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    password: constr(min_length=8)

    @validator('name')
    def validate_name_length(cls, name):
        if len(name) < 3:
            raise ValueError('Name should have at least 3 characters')
        return name

    @validator('age')
    def validate_age_range(cls, age):
        if age < 0 or age > 150:
            raise ValueError('Age should be between 0 and 150')
        return age

    @validator('password')
    def validate_password_length(cls, password):
        if len(password) < 8:
            raise ValueError('Password should have at least 8 characters')
        return password
