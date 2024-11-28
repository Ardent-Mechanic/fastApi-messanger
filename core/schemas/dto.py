from pydantic import BaseModel
from typing import Optional, List


class UserDTO(BaseModel):
    user_id: int
    phone_number: str
    name: str
    second_name: str
    middle_name: str

    class Config:
        from_attributes = True


class RoleDTO(BaseModel):
    role_id: int
    name: str

    class Config:
        from_attributes = True


class UserRoleBase(BaseModel):
    user_id: int
    role_id: int


class UserWithRoles(UserDTO):
    roles: List[UserDTO]


class RoleWithUsers(RoleDTO):
    users: List[RoleDTO]
