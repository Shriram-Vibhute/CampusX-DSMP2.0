# Abstraction - Abstract class - a class which have atleast 1 abstract method and you cannot create object ot these classes

from abc import ABC,abstractmethod
class BankApp(ABC):

  def database(self):
    print('connected to database')

  @abstractmethod
  def security(self):
    pass

  @abstractmethod
  def display(self):
    pass

class MobileApp(BankApp):

  def mobile_login(self):
    print('login into mobile')

  def security(self):
    print('mobile security')

  def display(self):
    print('display')

mob = MobileApp()

mob.security()

obj = BankApp()