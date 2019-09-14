class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "This account belongs to %s with balance $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print "$%.2f" % (self.balance)
  def deposit(self, amount):
    if amount <= 0:
      print "Error"
      return
    else:
      print "User deposit is $%.2f" % (amount)
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      print "Error again"
      return
    else:
      print "User withdtaws $%.2f" % (amount)
      self.balance -= amount
      self.show_balance()
      
my_account = BankAccount("Mary")
my_account.__repr__()
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
my_account.__repr__()