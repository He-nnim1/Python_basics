# classes
# Customer - names, email, kra, dob, gender
# BankAccount - Customer, acc_no, acc_type, balance

# self represents the customer herself
class Customer:
    def __init__(self, names:str, email:str, kra:str, dob:str, gender:str):
        self.names = names
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender

    def show_details(self):
        print(f"Name: {self.names} and KRA PIN: {self.kra} ")
        # return f"Name: {self.names} and KRA PIN: {self.kra}

    def __str__(self):
        return f"{self.names} "

class Account:
    def __init__(self, owner:Customer, acc_no:str, acc_type:str, balance:float):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("***********")

    def deposit(self, amount:float):
        self.balance += abs(amount)

    def withdraw(self, amount:float):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= abs(amount)
    def __str__(self):
        return f"Account no: {self.acc_no} for {self.owner.names}"





owner1 = Customer("Nina Jack", "nina@gmail.com", "KRA009", "21-09-2001", "F")
owner2 = Customer("Hudson Kinyanjui", "h@gmail.com", "KRA879", "03-01-1997", "")

acc1 = Account(owner1, "98334", "current", 76_000)
acc2 = Account(owner1, "98398", "savings", 100_789)
acc3 = Account(owner2, "61285", "current", 2_872_000)


# print(owner1.dob)
# print(owner1.show_details())

# acc1.print_details()
# acc1.deposit(-9000)
# acc1.print_details()
# acc1.withdraw(1_000)
# acc1.print_details()


print(owner1)
print(acc1)




