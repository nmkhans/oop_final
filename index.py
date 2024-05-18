from user import User
from admin import Admin
from bank import Bank


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