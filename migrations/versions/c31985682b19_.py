"""empty message

Revision ID: c31985682b19
Revises: 
Create Date: 2017-08-03 13:49:33.132664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c31985682b19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food_description',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ndbno_id', sa.String(), nullable=True),
    sa.Column('short_desc', sa.String(), nullable=True),
    sa.Column('food_cat', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('food_description')
    # ### end Alembic commands ###
