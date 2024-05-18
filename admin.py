from person import Person
from user import User

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