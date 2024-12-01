from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.model import Base


class Role(Base):
    role_id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, primary_key=True)

    users: Mapped[list['User']] = relationship('User', secondary='user_role', back_populates='roles')
