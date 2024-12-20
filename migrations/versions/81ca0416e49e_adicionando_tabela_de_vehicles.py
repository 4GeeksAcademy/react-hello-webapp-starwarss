"""Adicionando tabela de Vehicles

Revision ID: 81ca0416e49e
Revises: 0d7f0aa4c4c5
Create Date: 2024-12-12 10:57:03.384880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81ca0416e49e'
down_revision = '0d7f0aa4c4c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('model', sa.String(length=80), nullable=False),
    sa.Column('manufacturer', sa.String(length=80), nullable=False),
    sa.Column('passengers', sa.String(length=20), nullable=True),
    sa.Column('crew', sa.String(length=20), nullable=True),
    sa.Column('length', sa.String(length=20), nullable=True),
    sa.Column('max_atmosphering_speed', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vehicles_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'vehicles', ['vehicles_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('vehicles_id')

    op.drop_table('vehicles')
    # ### end Alembic commands ###
