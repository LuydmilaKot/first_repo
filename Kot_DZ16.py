from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, autoincrement=True, primary_key=True)
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


connection_string = "sqlite:///Kot_DZ16.sqlite"
engine = create_engine(connection_string)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

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


clients = session.query(Clients).all()
for client in clients:
    print(f"Client {client.name}:")
    for order in client.orders:
        print(f" {(order.name)}")
session.close()

connection = engine.connect()
query = connection.execute(
    text(
        "select clients.name as client_name, orders.name as order_name "
        "from clients JOIN orders on clients.id = orders.client_id"
    )
)
for i in query.mappings():
    print(f"Client {i['client_name']} ordered: {i['order_name']}")
connection.close()
