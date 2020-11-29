from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

engine = create_engine('sqlite:///houses.db', echo = True)

meta = MetaData()

houses = Table(
    'houses',
    meta,
    Column('id', Integer, primary_key = True),
    Column('Address', String),
    Column('CRIM', float),
    Column('ZN', float),
    Column('INDUS', float),
    Column('CHAS', float),
    Column('NOX', float),
    Column('RM', float),
    Column('AGE', float),
    Column('DIS', float),
    Column('RAD', float),
    Column('TAX', float),
    Column('PTRATIO', float),
    Column('B', float),
    Column('LSTAT', float)
)

meta.create_all(engine)