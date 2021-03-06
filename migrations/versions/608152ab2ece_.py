"""empty message

Revision ID: 608152ab2ece
Revises: 
Create Date: 2017-08-04 23:34:08.300000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '608152ab2ece'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
