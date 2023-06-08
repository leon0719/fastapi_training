from pydantic import BaseModel, Field, EmailStr, constr


class User(BaseModel):
    name: str = Field(...,
                      min_length=3,
                      description='Name should have at least 3 characters')
    age: int = Field(...,
                     gt=0,
                     lt=150,
                     description='Age should be between 0 and 150')
    email: EmailStr
    password: constr(min_length=8)
