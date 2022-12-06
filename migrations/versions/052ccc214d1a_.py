"""empty message

Revision ID: 052ccc214d1a
Revises: 70c68285d98f
Create Date: 2022-10-19 11:34:08.634851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '052ccc214d1a'
down_revision = '70c68285d98f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'quantity')
    # ### end Alembic commands ###