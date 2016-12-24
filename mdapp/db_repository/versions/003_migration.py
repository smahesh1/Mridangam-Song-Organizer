from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64), primary_key=True, nullable=False),
    Column('ragam', VARCHAR(length=64), primary_key=True, nullable=False),
    Column('artist', VARCHAR(length=64), primary_key=True, nullable=False),
    Column('link', VARCHAR(length=255)),
    Column('talam', VARCHAR(length=64)),
)

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
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['song'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['song'].drop()
