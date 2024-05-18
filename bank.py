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
