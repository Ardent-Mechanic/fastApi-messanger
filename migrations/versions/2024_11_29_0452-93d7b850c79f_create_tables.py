"""create tables

Revision ID: 93d7b850c79f
Revises: 
Create Date: 2024-11-29 04:52:16.202464

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "93d7b850c79f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "role",
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint("role_id", "name", name=op.f("pk_role")),
        sa.UniqueConstraint("name", name=op.f("uq_role_name")),
        sa.UniqueConstraint("role_id", name=op.f("uq_role_role_id")),
    )
    op.create_table(
        "user",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("phone_number", sa.String(length=50), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("second_name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint(
            "user_id", "phone_number", name=op.f("pk_user")
        ),
        sa.UniqueConstraint("phone_number", name=op.f("uq_user_phone_number")),
        sa.UniqueConstraint("user_id", name=op.f("uq_user_user_id")),
    )
    op.create_table(
        "user_role",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.role_id"],
            name=op.f("fk_user_role_role_id_role"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.user_id"],
            name=op.f("fk_user_role_user_id_user"),
        ),
        sa.PrimaryKeyConstraint(
            "user_id", "role_id", name=op.f("pk_user_role")
        ),
    )


def downgrade() -> None:
    op.drop_table("user_role")
    op.drop_table("user")
    op.drop_table("role")
