"""added quizAr, quizSt cols

Revision ID: 4fe31ef4e30e
Revises: 502d7ca01a73
Create Date: 2020-12-19 19:58:50.883680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fe31ef4e30e'
down_revision = '502d7ca01a73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('quizAr', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('quizSt', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'quizSt')
    op.drop_column('user', 'quizAr')
    # ### end Alembic commands ###
