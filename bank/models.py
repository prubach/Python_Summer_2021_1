from sqlalchemy import Numeric, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DBSession:
    current_db_session = None

    def engine(self):
        url = 'sqlite:///bank.db'
        return create_engine(url, echo=True)

    def get(self):
        """Opens a new database connection if there is none yet for the
        current application context.
        """
        if not DBSession.current_db_session:
            Session = sessionmaker(bind=self.engine(), autocommit=False, autoflush=False)
            current_db_session = Session()
        return current_db_session

# Create your models here.
class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(100))
    birth_date = Column(DateTime)

    def __init__(self, firstname, lastname, email, birth_date=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.birth_date = birth_date

    def __repr__(self):
        return "{} {} {} {}, {}".format(self.customer_id, self.firstname, self.lastname, self.email, self.birth_date)


class Account(Base):
    __tablename__ = 'account'
    account_id = Column(Integer, primary_key=True)
    balance = Column(Numeric)
    type = Column(String(20))
    customer = relationship('Customer')
    fk_customer_id = Column(Integer, ForeignKey(Customer.customer_id), index=True, nullable=False)

    def __init__(self, customer):
        self.customer = customer
        self.balance = 0
        self.type = 'Checking'

    def __repr__(self):
        return "{} {} {} {}".format(self.account_id, self.customer.last_name, self.type,self.balance)


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db_session = DBSession()
    Base.metadata.create_all(bind=db_session.engine())
