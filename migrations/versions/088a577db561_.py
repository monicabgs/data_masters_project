"""empty message

Revision ID: 088a577db561
Revises: 
Create Date: 2020-07-12 19:33:56.972082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '088a577db561'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_model',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('input_data', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model_result',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model_result', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('model_result')
    op.drop_table('data_model')
    # ### end Alembic commands ###
