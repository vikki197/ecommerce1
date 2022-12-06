"""empty message

Revision ID: df3f20751d8c
Revises: a94754d05111
Create Date: 2022-10-15 10:45:33.131278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3f20751d8c'
down_revision = 'a94754d05111'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False, auto_increment=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.String(length=20), nullable=True),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.Column('item_name', sa.String(length=600), nullable=True),
    sa.Column('order_price', sa.Integer(), nullable=True),
    sa.Column('sender_address', sa.String(length=600), nullable=True),
    sa.Column('address_name', sa.String(length=400), nullable=True),
    sa.Column('delivery_address', sa.String(length=600), nullable=True),
    sa.Column('delivery_date', sa.DateTime(), nullable=True),
    sa.Column('payment_details', sa.String(length=600), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###