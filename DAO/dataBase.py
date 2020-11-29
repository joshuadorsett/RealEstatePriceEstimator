from sqlalchemy import *


class DB:

    def __init__(self):
        self.db = create_engine('sqlite:///houses.db', echo = True)
        self.meta = MetaData()
        self.houses = Table (
            'Houses',
            self.meta,
            Column('id', Integer, primary_key=True),
            Column('address', String),
            Column('crim', Float),
            Column('zn', Float),
            Column('indus', Float),
            Column('chas', Float),
            Column('nox', Float),
            Column('rm', Float),
            Column('age', Float),
            Column('dis', Float),
            Column('rad', Float),
            Column('tax', Float),
            Column('ptratio', Float),
            Column('b', Float),
            Column('lstat', Float)
        )
        self.meta.create_all(self.db)
        self.conn = self.db.connect()

    def insert(self, house):
        selAddress = self.select(house.address)
        if selAddress is None:
            insert = self.houses.insert().values(
                address=house.address,
                crim=house.houseSpecs[0][0],
                zn=house.houseSpecs[0][1],
                indus=house.houseSpecs[0][2],
                chas=house.houseSpecs[0][3],
                nox=house.houseSpecs[0][4],
                rm=house.houseSpecs[0][5],
                age=house.houseSpecs[0][6],
                dis=house.houseSpecs[0][7],
                rad=house.houseSpecs[0][8],
                tax=house.houseSpecs[0][9],
                ptratio=house.houseSpecs[0][10],
                b=house.houseSpecs[0][11],
                lstat=house.houseSpecs[0][12]
            )
            self.conn.execute(insert)
        else:
            update = self.houses.update().values(
                address=house.address,
                crim=house.houseSpecs[0][0],
                zn=house.houseSpecs[0][1],
                indus=house.houseSpecs[0][2],
                chas=house.houseSpecs[0][3],
                nox=house.houseSpecs[0][4],
                rm=house.houseSpecs[0][5],
                age=house.houseSpecs[0][6],
                dis=house.houseSpecs[0][7],
                rad=house.houseSpecs[0][8],
                tax=house.houseSpecs[0][9],
                ptratio=house.houseSpecs[0][10],
                b=house.houseSpecs[0][11],
                lstat=house.houseSpecs[0][12]
            ).where(self.houses.c.address == house.address)
            self.conn.execute(update)
            print("already in DB")
    def selectAll(self):
        sel = self.houses.select()
        r = self.conn.execute(sel)
        return r.fetchall()

    def select(self, address):
        sel = self.houses.select().where(self.houses.c.address.like(address))
        r = self.conn.execute(sel)
        return r.fetchone()

    def delete(self, address):
        delete = self.houses.delete().where(self.houses.c.address.like(address))
        self.conn.execute(delete)