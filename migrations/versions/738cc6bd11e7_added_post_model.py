"""added post model

Revision ID: 738cc6bd11e7
Revises: 6182eaac0249
Create Date: 2022-07-12 14:36:41.059475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '738cc6bd11e7'
down_revision = '6182eaac0249'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###