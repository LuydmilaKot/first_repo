from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select
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


def get_orders():
    session = Session()
    stmt = session.execute(select(Orders))
    my_orders = stmt.scalars().all()
    session.close()
    return my_orders
