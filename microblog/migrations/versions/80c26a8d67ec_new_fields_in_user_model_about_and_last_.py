"""new fields in user model: about and last seen

Revision ID: 80c26a8d67ec
Revises: 30447cc63047
Create Date: 2022-04-28 14:58:23.380244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80c26a8d67ec'
down_revision = '30447cc63047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###