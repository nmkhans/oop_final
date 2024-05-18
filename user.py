import random
from person import Person
from transaction import Transaction
from datetime import datetime

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
    
       