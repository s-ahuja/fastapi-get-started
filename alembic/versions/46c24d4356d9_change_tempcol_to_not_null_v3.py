"""change tempcol to not null-v3

Revision ID: 46c24d4356d9
Revises: 78f91882202d
Create Date: 2021-09-05 16:53:05.668694

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '46c24d4356d9'
down_revision = '78f91882202d'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("UPDATE items set tempcol=''")
    op.alter_column('items', 'tempcol', existing_type=sa.VARCHAR(length=20), nullable=False)
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'tempcol', existing_type=sa.VARCHAR(length=20), nullable=True)
    # ### end Alembic commands ###
