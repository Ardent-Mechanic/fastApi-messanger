from pydantic import BaseModel
from pydantic import ConfigDict


class RoleBase(BaseModel):
    role_id: int
    name: str


class RolePut(RoleBase):
    pass


class UserGet(RoleBase):
    pass
