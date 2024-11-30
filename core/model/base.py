from sqlalchemy import String, ForeignKey, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr, relationship

from core.config import settings
from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}"


# class User(Base):
#     user_id: Mapped[int] = mapped_column(unique=True, primary_key=True)
#     phone_number: Mapped[str] = mapped_column(String(50), unique=True, primary_key=True)
#     name: Mapped[str] = mapped_column(String(50))
#     second_name: Mapped[str] = mapped_column(String(50))
#     last_name: Mapped[str] = mapped_column(String(50))
#
#     roles: Mapped[list['Role']] = relationship('Role', secondary='user_role', back_populates='users')


# class Role(Base):
#     role_id: Mapped[int] = mapped_column(unique=True, primary_key=True)
#     name: Mapped[str] = mapped_column(String(30), unique=True, primary_key=True)
#
#     users: Mapped[list['User']] = relationship('User', secondary='user_role', back_populates='roles')


# class UserRole(Base):
#     user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'), primary_key=True)
#     role_id: Mapped[int] = mapped_column(ForeignKey('role.role_id'), primary_key=True)
#
#     user: Mapped['User'] = relationship('User', back_populates='roles')
#     role: Mapped['Role'] = relationship('Role', back_populates='users')
