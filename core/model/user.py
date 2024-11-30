from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.model import Base
from core.model import Role


class User(Base):
    user_id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    phone_number: Mapped[str] = mapped_column(String(50), unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    second_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    roles: Mapped[list['Role']] = relationship('Role', secondary='user_role', back_populates='users')
