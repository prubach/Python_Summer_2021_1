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
        if amount <= 0:
            raise IncorrectAmountException("Incorrect amount")
        self._balance += amount

    def charge(self, amount):
        if amount < 0:
            raise IncorrectAmountException("Incorrect amount")
        if amount > self._balance:
            raise InsufficientBalanceException("Insufficient Balance, current balance is: " + self._balance)
        self._balance -= amount

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance)


class BankException(Exception):
    pass

class IncorrectAmountException(BankException):
    pass

class InsufficientBalanceException(BankException):
    pass


c1 = Customer('Anna', 'Smith')
print(c1)
c2 = Customer('John', 'Brown')
print(c2)
a1 = Account(c1)
a2 = Account(c2)
a3 = Account(c2)
print(a1)
a1.deposit(100)
print(a1)
a1.deposit(-50)
print(a1)
a1.charge(80)
print(a1)
