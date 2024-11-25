from pydantic import BaseModel
from typing import Optional, List


class UserDTO(BaseModel):
    phone_number: str
    name: str
    second_name: str
    middle_name: str

    class Config:
        from_attributes = True
