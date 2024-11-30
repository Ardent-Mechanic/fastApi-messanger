from pydantic import BaseModel
from pydantic import ConfigDict


class UserBase(BaseModel):
    user_id: int
    phone_number: str
    name: str
    second_name: str
    middle_name: str

    class Config:
        from_attributes = True


class UserPut(UserBase):
    pass


class UserGet(UserBase):
    pass
