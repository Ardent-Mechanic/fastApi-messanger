from pydantic import BaseModel
from pydantic import ConfigDict


class UserRoleBase(BaseModel):
    user_id: int
    role_id: int


class UserRolePut(UserRoleBase):
    pass


class UserRoleGet(UserRoleBase):
    pass
