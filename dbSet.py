import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Sequence, JSON, UniqueConstraint
import pymysql
pymysql.install_as_MySQLdb()
import json
engine = create_engine('mysql://root:password@127.0.0.1/contextO')
conn = engine.connect()

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
    Column('nombre', String(50), unique=True),
    Column('data', JSON())
)

metadata.create_all(engine)

with open('dataModel.json', 'r') as f:
    dataModel_dict = json.load(f)
    conn.execute(users.insert(), dataModel_dict)




