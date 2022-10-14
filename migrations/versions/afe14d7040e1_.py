"""empty message

Revision ID: afe14d7040e1
Revises: 
Create Date: 2022-10-14 01:37:16.745439

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "afe14d7040e1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("email", sa.String(length=45), nullable=True),
        sa.Column("salary", sa.Numeric(precision=15, scale=2), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "expense",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("value", sa.Numeric(precision=14, scale=2), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("color", sa.String(length=40), nullable=True),
        sa.Column("total", sa.Numeric(precision=14, scale=2), nullable=True),
        sa.Column("due_date", sa.Date(), nullable=True),
        sa.Column("status", sa.Enum("active", "cancelled", name="expensestatus"), nullable=True),
        sa.Column("paid", sa.Boolean(), nullable=True),
        sa.Column("profile_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profiles.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("expense")
    op.drop_table("profiles")
    # ### end Alembic commands ###