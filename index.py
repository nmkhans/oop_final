import random
from datetime import datetime

# All classes

class Bank:
  def __init__(self, name, initial_balance):
    self.name = name
    self.balance = initial_balance
    self.total_loan = 0
    self.users = []
    self.admins = []
    self.loan_taken = {} # {"moin": 2}
    self.__loan_feature = True

  def add_user(self, user):
    self.users.append(user)

  def grant_loan(self, user, amount):
    if self.__loan_feature == False:
      print("Loan is not available at this moment.")
      return

    if amount <= self.balance:
      if self.loan_taken.get(user.name):
        if self.loan_taken.get(user.name) < 2:
          self.loan_taken[user.name] += 1
          self.balance -= amount
          user.balance += amount
          self.total_loan += amount

          print(f"{amount} Money has been taken loan.")
          return True
        else:
          print("Loan taking has reached its limit. Repay first two loan")
      else:
        self.loan_taken[user.name] = 1
        self.balance -= amount
        user.balance += amount
        self.total_loan += amount

        print(f"{amount} Money has been taken loan.")
        return True
    else:
      print("Your request amount exceeded banks balance")

  def check_loan_taken_list(self):
    for keys, values in self.loan_taken.items():
      print(f"Name: {keys}, taken: {values} times")

  @property
  def loan_feature(self):
    print(self.__loan_feature)

  @loan_feature.setter
  def loan_feature(self, decision):
    self.__loan_feature = decision


class Person:
  def __init__(self, name, email, password, address):
    self.name = name
    self.email = email
    self.password = password
    self.address = address

class Transaction:
  def __init__(self, type, amount, date):
    self.type = type
    self.amount = amount
    self.date = date

class Admin(Person):
  def __init__(self, name, email, password, address, bank):
    super().__init__(name, email, password, address)
    self.account_status = "admin"
    self.bank = bank

  def create_account(self, name, email, password, address, acc_type):
    user = User(name, email, password, address, acc_type, self.bank)
    self.bank.users.append(user)

  def delete_user(self, name):
    user = {}

    for person in self.bank.users:
      if person.name.lower() == name.lower():
        user = person
        break

    if user == {}:
      print("No user found!")
      return
    
    self.bank.users.remove(user)
    print("User has been deleted!")

  def user_account_list(self):
    if self.bank.users != []:
      print("Name:\tBalance: Acc_type: Loan taken:")

      for person in self.bank.users:
        print(f"{person.name}\t{person.balance}\t{person.account_type}\t{self.bank.loan_taken.get(person.name) and self.bank.loan_taken.get(person.name) or "No"}")
    else:
      print("No users available!")

  def admin_list(self):
    print("Name:\tEmail:")

    for person in self.bank.admins:
      print(f"{person.name}\t{person.email}")

  def check_total_balance(self):
    print(f"Bank name: {self.bank.name}, Total balance: {self.bank.balance} ")

  def check_total_loan_amount(self):
    print(f"Bank name: {self.bank.name}, Total loan on pending: {self.bank.total_loan} ")

  def toggle_loan_feture(self, decision):
    self.bank.loan_feature = decision

class User(Person):
  def __init__(self, name, email, password, address, account_type, bank):
    super().__init__(name, email, password, address)
    self.account_type = account_type
    self.balance = 0
    self.account_no = self.gen_acc_no()
    self.bank = bank
    self.transaction_history = []

  def gen_acc_no(self):
    list_of_word = {
      0: "a",
      1: "b",
      2: "c",
      3: "d",
      4: "e",
      5: "f",
      6: "g",
      7: "h",
      8: "i",
      9: "j",
    }

    acc_no = ""
    while len(acc_no) < 5:
      random_char = random.randint(0, 9)
      if list_of_word[random_char] not in acc_no:
        acc_no += list_of_word[random_char]

    return acc_no

  def deposit_amount(self, amount):
    if amount > 0:
      self.balance += amount
      self.bank.balance += amount

      transaction = Transaction("deposit", amount, datetime.now())
      self.transaction_history.append(transaction)

      print(f"{amount} money has been added into your balance.")
    else:
      print("Invalid deposit amount!")
      return

  def withdraw_amount(self, amount):
    if self.bank.balance == 0:
      print("The bank is bankrupted!")
      return
    elif amount > self.bank.balance:
      print("Invalid withdraw amount!")
      return
    
    if amount <= self.balance:
      self.balance -= amount
      self.bank.balance -= amount

      transaction = Transaction("withdraw", amount, datetime.now())
      self.transaction_history.append(transaction)

      print(f"{amount} money has been withdrawed.")
    else:
      print("Withdrawal amount exceeded")
      return
    
  def check_balance(self):
    print(f"Your current balance is: {self.balance}")
  
  def check_transaction_history(self):
    if self.transaction_history:
      for history in self.transaction_history:
        print(f"Date: {history.date}")
        print(f"Transaction type: {history.type} Amount: {history.amount}")
    else:
      print("No history available!")

  def take_loan(self, amount):
    loan = self.bank.grant_loan(self, amount)

    if loan:
      transaction = Transaction("loan taken", amount, datetime.now())
      self.transaction_history.append(transaction)

  def transfer_balance(self, name, amount):
    reciver = {}

    for person in self.bank.users:
      if person.name.lower() == name.lower():
        reciver = person
        break

    if reciver == {}:
      print("Account does not exist!")
      return   
    
    if amount <= self.balance:
      reciver.balance += amount
      self.balance -= amount

      transaction = Transaction("balance transfered", amount, datetime.now())
      self.transaction_history.append(transaction)

      print("Money Transfer successfull")
    else:
      print("Transfer request exceeded from balance!")
    



dutch_bangla = Bank("Dutch Bangla", 50000)
admin = Admin("admin", "admin@gmail.com", "admin123", "Savar, dhaka", dutch_bangla)
moin = User("moin", "moin@gmail.com", "123", "dhaka", "savings", dutch_bangla)
dutch_bangla.admins.append(admin)
dutch_bangla.users.append(moin)

current_user = None

while True:
  if current_user == None:
    print(f"-----Welcome to Bank {dutch_bangla.name}-----")
    print("Choose a option from below:")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    option = int(input("Enter option: "))

    if option == 1:
      print("---User login/register---")
      choice = input("Login or Register(L/R): ")

      if choice.lower() == "l":
        print("---Welcome back---")
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        for person in dutch_bangla.users:
          if person.name.lower() == name.lower():
            if person.password == password:
              current_user = person
              print("Login successfull.")
              break
            else:
              print("Invalid password!")
              break

        if current_user == None:
          print(f"No user found named {name}")

      elif choice.lower() == "r":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        address = input("Enter your address: ")
        account_type = input("Enter your account_type(savings/current) : ")
        
        user = User(name, email, password, address, account_type, dutch_bangla)
        current_user = user
        dutch_bangla.users.append(user)

        print("Registration successfull.")
    elif option == 2:
      print("---Admin login/register---")
      choice = input("Login or Register(L/R): ")

      if choice.lower() == "l":
        print("---Welcome back---")
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        for person in dutch_bangla.admins:
          if person.name.lower() == name.lower():
            if person.password == password:
              current_user = person
              print("Login successfull.")
              break
            else:
              print("Invalid password!")
              break

        if current_user == None:
          print(f"No admin found named {name}")

      elif choice.lower() == "r":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        address = input("Enter your address: ")
        
        admin = Admin(name, email, password, address, dutch_bangla)
        current_user = admin
        dutch_bangla.admins.append(admin)

        print("Registration successfull.")

    elif option == 3:
      break
    else:
      print("Invalid input!")

  elif current_user.name == "admin":
    print(f"Welcome back admin {current_user.name}")
    print("Choose a option from below: ")
    print("1. create account")
    print("2. delete user")
    print("3. see all user")
    print("4. check total balance")
    print("5. check total loan")
    print("6. toggle loan")
    print("7. Exit")

    option = int(input("Enter option: "))

    if option == 1:
      print("---create user account---")
      name = input("Enter your name: ")
      email = input("Enter your email: ")
      password = input("Enter your password: ")
      address = input("Enter your address: ")
      account_type = input("Enter your account_type(savings/current) : ")

      current_user.create_account(name, email, password, address, account_type)
      print("User added successfully.")

    elif option == 2:
      print("---delete user---")
      name = input("Enter name: ")

      current_user.delete_user(name)

    elif option == 3:
      print("---all users list---")      
      current_user.user_account_list()

    elif option == 4:
      print("---total balance amount---")
      current_user.check_total_balance()

    elif option == 5:
      print("---total loan amount---")
      current_user.check_total_loan_amount()

    elif option == 6:
      print("---toggle loan feature---")
      option = input("Enter decision(on/off): ")

      if option == "on":
        current_user.toggle_loan_feture(True)
      elif option == "off":
        current_user.toggle_loan_feture(False)
    elif option == 7:
      current_user = None
    else:
      print("Invalid input")

  else:
    print(f"Welcome back user {current_user.name}")
    print("Choose a option from below: ")
    print("1. deposit amount")
    print("2. withdraw amount")
    print("3. check balance")
    print("4. check transaction history")
    print("5. take loan")
    print("6. transfer balance")
    print("7. Exit")

    option = int(input("Enter a option: "))

    if option == 1:
      amount = int(input("Enter a amount: "))
      current_user.deposit_amount(amount)
    elif option == 2:
      amount = int(input("Enter a amount: "))
      current_user.withdraw_amount(amount)
    elif option == 3:
      current_user.check_balance()
    elif option == 4:
      current_user.check_transaction_history()
    elif option == 5:
      amount = int(input("Enter a amount: "))
      current_user.take_loan(amount)
    elif option == 6:
      name = input("Enter reciver name: ")
      amount = int(input("Enter a amount: "))

      current_user.transfer_balance(name, amount)
    elif option == 7:
      current_user = None
    else:
      print("Invalid input")