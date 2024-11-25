from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr, relationship

from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}"


class User(Base):
    phone_number: Mapped[str] = mapped_column(String(50), unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    second_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

