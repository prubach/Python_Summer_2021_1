class Customer:
    last_id=0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)


class Account:
    last_id = 0
    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        #todo
        pass

    def charge(self, amount):
        #TODO
        pass

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance)



c1 = Customer('Anna', 'Smith')
print(c1)
c2 = Customer('John', 'Brown')
print(c2)
a1 = Account(c1)
a2 = Account(c2)
a3 = Account(c2)
print(a1)
print(a2)
print(a3)
