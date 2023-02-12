"""initial migration

Revision ID: 17cf62fbb232
Revises: 
Create Date: 2023-02-12 22:07:54.819245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17cf62fbb232'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_map',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original', sa.String(length=256), nullable=False),
    sa.Column('short', sa.String(length=16), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('url_map')
    # ### end Alembic commands ###
