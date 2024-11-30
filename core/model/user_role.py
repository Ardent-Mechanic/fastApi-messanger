from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.model import Base, User, Role


class UserRole(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('role.role_id'), primary_key=True)

    user: Mapped['User'] = relationship('User', back_populates='roles')
    role: Mapped['Role'] = relationship('Role', back_populates='users')
