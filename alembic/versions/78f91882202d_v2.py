"""v2

Revision ID: 78f91882202d
Revises: 9b4aa6ba4f79
Create Date: 2021-09-05 16:50:40.431889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78f91882202d'
down_revision = '9b4aa6ba4f79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('tempcol', sa.String(length=20), nullable=True))
    op.alter_column('items', 'title',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('items', 'description',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'description',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('items', 'title',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.drop_column('items', 'tempcol')
    # ### end Alembic commands ###
