"""empty message

Revision ID: 0581c2e58484
Revises: 1ba95ed6a44d
Create Date: 2022-10-15 16:57:53.310703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0581c2e58484'
down_revision = '1ba95ed6a44d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.String(length=20), nullable=True),
    sa.Column('product_name', sa.String(length=120), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('pics', sa.ARRAY(sa.LargeBinary()), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    # ### end Alembic commands ###
