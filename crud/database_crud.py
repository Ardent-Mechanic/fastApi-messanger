from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from core.model import  db_helper, User
from core.schemas.dto import UserDTO

# Session = sessionmaker(bind=db_helper.engine)


# session = Session()


# session = Session()


# def get_user(user_id: str):
#     session = Session()
#     return session.query()
#
#
# def add_user(user: UserDTO):
#     session = Session()
#     session.add(user)
#     session.commit()
#     session.close()
#
#
# def get_migration_service(user_id: str):
#     session = Session()
#     return session.query()
#
#
# def add_migration_service(migration_service: MigrationServiceDTO):
#     session = Session()
#     session.add(migration_service)
#     session.commit()
#     session.close()


# def get_investment(investment_id: str):
#     session = Session()
#     return session.query()


# def add_investment(dto: InvestmentDTO):
#     investment = Investment(
#         id=dto.id,
#         years=dto.years,
#         money=dto.money,
#         portfolio_type_id=dto.portfolio_type_id
#     )
#     session = Session()
#     session.add(investment)
#     session.commit()
#     session.close()


async def get_one_user(session: AsyncSession, user_phone: str):
    stmt = select(User).where(User.phone_number == user_phone)
    result = await session.scalars(stmt)

    return result.all() if result else {}
# add_investment(**{
#     "id": 1,
#     "years": 1,
#     "money": 1000,
#     "portfolio_type_id": 1
# })

# add_migration_service(MigrationServiceDTO(**{
#     "new_citizenship": True,
#     "only_ru": True,
#     "insurance": True,
#     "insurance_deposite": 100
# }))

# add_user(UserDTO(**{
#     "phone_number": "1234567890",
#     "name": "John",
#     "second_name": "Doe",
#     "last_name": "M",
#     "investment_id": 1,
#     "migration_service_id": 1
# }))
