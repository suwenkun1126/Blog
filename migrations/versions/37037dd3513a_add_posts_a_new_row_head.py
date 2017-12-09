"""add posts a new row:head

Revision ID: 37037dd3513a
Revises: 539dae032031
Create Date: 2017-12-01 21:14:48.627000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37037dd3513a'
down_revision = '539dae032031'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('head', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'head')
    # ### end Alembic commands ###
