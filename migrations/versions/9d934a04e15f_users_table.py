"""users table

Revision ID: 9d934a04e15f
Revises: 
Create Date: 2020-05-18 16:26:20.633103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d934a04e15f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('task',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('author_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['author_name'], ['author.name'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('author')
    # ### end Alembic commands ###
