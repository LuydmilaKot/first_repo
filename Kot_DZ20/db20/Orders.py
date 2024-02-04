from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    orders = relationship("Orders", back_populates="client")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    cost = Column(Integer)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Clients", back_populates="orders")

    def __init__(self, name, cost, client_id):
        self.name = name
        self.cost = cost
        self.client_id = client_id

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


connection_string = "sqlite:///C:\/Users\Людмила\PycharmProjects\Prob\TeachMeSkills\Kot_DZ16.sqlite"
engine = create_engine(connection_string)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# session = Session()
#
# petya = Clients('Petya')
# ira = Clients('Ira')
# vasya = Clients('Vasya')
# sasha = Clients('Sasha')
# or_1 = Orders("sofa", 10, 1)
# or_2 = Orders("armchair", 7, 2)
# or_3 = Orders("table", 560, 2)
# or_4 = Orders("chair", 350, 3)
# or_5 = Orders("bed", 25, 4)
# or_6 = Orders("lamp", 2, 1)
# or_7 = Orders("carpet", 35, 1)
# or_8 = Orders("fridge", 4, 3)
# or_9 = Orders("toilet", 90, 3)
# or_10 = Orders("bath", 10, 1)
# or_11 = Orders("leptop", 20, 4)
# session.add_all([petya, ira, vasya, sasha, or_1, or_2, or_3, or_4, or_5, or_6, or_7, or_8, or_9, or_10])
#
# session.commit()

def get_orders():
    session = Session()
    stmt = session.execute(select(Orders))
    all_orders = stmt.scalars().all()
    session.close()
    return all_orders


def create_orders(name, cost, client_id):
    session = Session()
    new_order = Orders(name=name, cost=cost, client_id=client_id)
    session.add(new_order)
    session.commit()
    session.close()
    return new_order


def delete_orders(client_id):
    session = Session()
    order = session.query(Orders).filter_by(id=client_id).first()
    if order:
        # Удаление заказа из базы данных
        session.delete(order)
        session.commit()
    session.close()


def create_client(name):
    session = Session()
    new_client = Clients(name)
    session.add(new_client)
    session.commit()
    session.close()
    return new_client


def get_clients():
    session = Session()
    stmt = session.execute(select(Clients))
    all_clients = stmt.scalars().all()
    session.close()
    return all_clients


def delete_clients(client_id):
    session = Session()
    client = session.query(Clients).filter_by(id=client_id).first()
    if client:
        # Удаление клиента из базы данных
        session.delete(client)
        session.commit()
    session.close()
