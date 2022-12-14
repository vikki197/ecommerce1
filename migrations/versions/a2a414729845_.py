"""empty message

Revision ID: a2a414729845
Revises: 75fe264dd815
Create Date: 2022-10-14 10:17:49.257044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2a414729845'
down_revision = '75fe264dd815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('timezone', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'timezone')
    # ### end Alembic commands ###
