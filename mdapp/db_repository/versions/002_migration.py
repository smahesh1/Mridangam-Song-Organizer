from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
song = Table('song', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64), primary_key=True, nullable=False),
    Column('ragam', String(length=64), primary_key=True, nullable=False),
    Column('talam', String(length=64)),
    Column('artist', String(length=64), primary_key=True, nullable=False),
    Column('link', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['song'].columns['talam'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['song'].columns['talam'].drop()
