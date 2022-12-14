"""empty message

Revision ID: 1a8881143464
Revises: c6cb4294c5e6
Create Date: 2022-10-20 19:21:05.412837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a8881143464'
down_revision = 'c6cb4294c5e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventoryuser', sa.Column('admin_id', sa.String(length=20), nullable=True))
    op.drop_column('inventoryuser', 'gender')
    op.drop_column('inventoryuser', 'contact_number')
    op.drop_column('inventoryuser', 'name')
    op.drop_column('inventoryuser', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventoryuser', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('inventoryuser', sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('inventoryuser', sa.Column('contact_number', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('inventoryuser', sa.Column('gender', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('inventoryuser', 'admin_id')
    # ### end Alembic commands ###
