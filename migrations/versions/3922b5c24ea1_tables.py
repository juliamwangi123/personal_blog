"""tables

Revision ID: 3922b5c24ea1
Revises: cc46ddd0d5c7
Create Date: 2022-05-14 13:06:52.147233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3922b5c24ea1'
down_revision = 'cc46ddd0d5c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('sub_title', sa.String(length=120), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blog_title'), 'blog', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blog_title'), table_name='blog')
    op.drop_table('blog')
    op.drop_table('user')
    # ### end Alembic commands ###
