from sqlalchemy import *


class DB:
    # connect to database and create the house table schema
    def __init__(self):
        self.db = create_engine('sqlite:///houses.db', echo=True)
        self.meta = MetaData()
        self.houses = Table(
            'Houses',
            self.meta,
            Column('id', Integer, primary_key=True),
            Column('salesid', String),
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

    # insert a new house into the house table if its a new address
    # update a previous house if address is already in house table
    def insert(self, house):
        selSalesId = self.select(house.salesId)
        if selSalesId is None:
            ins = self.houses.insert().values(
                salesid=house.salesId,
                crim=house.houseSpecs[0],
                zn=house.houseSpecs[1],
                indus=house.houseSpecs[2],
                chas=house.houseSpecs[3],
                nox=house.houseSpecs[4],
                rm=house.houseSpecs[5],
                age=house.houseSpecs[6],
                dis=house.houseSpecs[7],
                rad=house.houseSpecs[8],
                tax=house.houseSpecs[9],
                ptratio=house.houseSpecs[10],
                b=house.houseSpecs[11],
                lstat=house.houseSpecs[12]
            )
            self.conn.execute(ins)
        else:
            upd = self.houses.update().values(
                salesid=house.salesId,
                crim=house.houseSpecs[0],
                zn=house.houseSpecs[1],
                indus=house.houseSpecs[2],
                chas=house.houseSpecs[3],
                nox=house.houseSpecs[4],
                rm=house.houseSpecs[5],
                age=house.houseSpecs[6],
                dis=house.houseSpecs[7],
                rad=house.houseSpecs[8],
                tax=house.houseSpecs[9],
                ptratio=house.houseSpecs[10],
                b=house.houseSpecs[11],
                lstat=house.houseSpecs[12]
            ).where(self.houses.c.salesid == house.salesId)
            self.conn.execute(upd)
            print("already in DB")

    # return all rows from house table
    def selectAll(self):
        sel = self.houses.select()
        r = self.conn.execute(sel)
        return r.fetchall()

    # return a specific row from house table
    def select(self, salesid):
        sel = self.houses.select().where(self.houses.c.salesid.like(salesid))
        r = self.conn.execute(sel)
        return r.fetchone()

    # delete a specific row from the house table
    def delete(self, salesid):
        dele = self.houses.delete().where(self.houses.c.salesid.like(salesid))
        self.conn.execute(dele)
