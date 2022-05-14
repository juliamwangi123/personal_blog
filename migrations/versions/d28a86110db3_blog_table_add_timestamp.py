"""blog table add timestamp

Revision ID: d28a86110db3
Revises: 0d6c3dc15a63
Create Date: 2022-05-14 23:05:55.815130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd28a86110db3'
down_revision = '0d6c3dc15a63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('Timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'Timestamp')
    # ### end Alembic commands ###
