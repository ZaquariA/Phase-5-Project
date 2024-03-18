"""empty message

Revision ID: 95324d8b3a89
Revises: 
Create Date: 2024-03-18 08:43:20.709411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95324d8b3a89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hobbies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('comments', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('friend',
    sa.Column('friend1_id', sa.Integer(), nullable=True),
    sa.Column('friend2_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['friend1_id'], ['users.id'], name=op.f('fk_friend_friend1_id_users')),
    sa.ForeignKeyConstraint(['friend2_id'], ['users.id'], name=op.f('fk_friend_friend2_id_users'))
    )
    op.create_table('post_hobbies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('hobby_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hobby_id'], ['hobbies.id'], name=op.f('fk_post_hobbies_hobby_id_hobbies')),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name=op.f('fk_post_hobbies_post_id_posts')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_hobbies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('hobby_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hobby_id'], ['hobbies.id'], name=op.f('fk_user_hobbies_hobby_id_hobbies')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_hobbies_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name=op.f('fk_user_posts_post_id_posts')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_posts_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_posts')
    op.drop_table('user_hobbies')
    op.drop_table('post_hobbies')
    op.drop_table('friend')
    op.drop_table('users')
    op.drop_table('posts')
    op.drop_table('hobbies')
    # ### end Alembic commands ###