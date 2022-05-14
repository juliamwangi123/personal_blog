"""tables

Revision ID: 2238ff16108c
Revises: 920c8097c949
Create Date: 2022-05-14 20:45:09.098587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2238ff16108c'
down_revision = '920c8097c949'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('sub_title', sa.String(length=120), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blog_title'), 'blog', ['title'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_blog_title'), table_name='blog')
    op.drop_table('blog')
    # ### end Alembic commands ###