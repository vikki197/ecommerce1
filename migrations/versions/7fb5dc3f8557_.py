"""empty message

Revision ID: 7fb5dc3f8557
Revises: 
Create Date: 2022-10-13 18:59:20.013597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fb5dc3f8557'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.String(length=20), nullable=False),
    sa.Column('product_name', sa.String(length=120), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('manufacturer_address', sa.String(length=220), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('pics', sa.ARRAY(sa.LargeBinary()), nullable=True),
    sa.Column('description', sa.String(length=320), nullable=True),
    sa.Column('product_tag', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=16), nullable=False),
    sa.Column('user_mail', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('user_mail')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('products')
    # ### end Alembic commands ###
