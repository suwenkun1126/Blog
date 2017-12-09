"""add posts a new row visits

Revision ID: 938de4f63b0c
Revises: f28e4cf33f7e
Create Date: 2017-12-06 21:18:01.010000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '938de4f63b0c'
down_revision = 'f28e4cf33f7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('visits', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'visits')
    # ### end Alembic commands ###
