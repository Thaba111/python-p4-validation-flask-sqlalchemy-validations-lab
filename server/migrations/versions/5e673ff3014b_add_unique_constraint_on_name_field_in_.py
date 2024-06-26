"""Add unique constraint on name field in Author model

Revision ID: 5e673ff3014b
Revises: faa482c1e292
Create Date: 2024-04-12 07:30:41.596523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e673ff3014b'
down_revision = 'faa482c1e292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('category',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('summary',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('summary',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('category',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('content',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
