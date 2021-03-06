"""empty message

Revision ID: 0e52c347db0e
Revises: 
Create Date: 2022-05-24 15:25:30.699733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e52c347db0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('common_weapon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weapon_name', sa.String(length=120), nullable=False),
    sa.Column('weapon_type', sa.String(length=20), nullable=False),
    sa.Column('weapon_class', sa.String(length=20), nullable=False),
    sa.Column('weapon_lore', sa.String(length=1000), nullable=False),
    sa.Column('location_description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exotic_weapon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weapon_name', sa.String(length=120), nullable=False),
    sa.Column('weapon_type', sa.String(length=20), nullable=False),
    sa.Column('weapon_class', sa.String(length=20), nullable=False),
    sa.Column('weapon_lore', sa.String(length=1000), nullable=False),
    sa.Column('location_description', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('legendary_weapon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weapon_name', sa.String(length=120), nullable=False),
    sa.Column('weapon_type', sa.String(length=20), nullable=False),
    sa.Column('weapon_class', sa.String(length=20), nullable=False),
    sa.Column('weapon_lore', sa.String(length=1000), nullable=False),
    sa.Column('location_description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rare_weapon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weapon_name', sa.String(length=120), nullable=False),
    sa.Column('weapon_type', sa.String(length=20), nullable=False),
    sa.Column('weapon_class', sa.String(length=20), nullable=False),
    sa.Column('weapon_lore', sa.String(length=1000), nullable=False),
    sa.Column('location_description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('star_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('uncommon_weapon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weapon_name', sa.String(length=120), nullable=False),
    sa.Column('weapon_type', sa.String(length=20), nullable=False),
    sa.Column('weapon_class', sa.String(length=20), nullable=False),
    sa.Column('weapon_lore', sa.String(length=1000), nullable=False),
    sa.Column('location_description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('dob', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('uncommon_weapon')
    op.drop_table('star_rating')
    op.drop_table('rare_weapon')
    op.drop_table('legendary_weapon')
    op.drop_table('exotic_weapon')
    op.drop_table('common_weapon')
    # ### end Alembic commands ###
