from models import DBSession, init_db, Customer, Account
import datetime

def add():
    init_db()
    c1 = Customer('Anna', 'Smith', 'anna@smith.com', datetime.datetime(1990, 5, 1))
    c2 = Customer('John', 'Brown', 'anna@brown.com', datetime.datetime(1992, 5, 1))
    print(c1)
    a1 = Account(c1)
    a2 = Account(c2)
    db = DBSession().get()
    db.add(c1)
    db.add(c2)
    db.add(a1)
    db.add(a2)
    db.commit()

db = DBSession().get()
customers = db.query(Customer).filter(Customer.lastname=='Brown').all()
print(customers)