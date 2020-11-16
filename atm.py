class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("balance is 50000")

    def withdrawl(self,amountno):
        newamount = 50000 - amountno
        print("you have withdrawn amount "+str(amountno) +". Your remaining balance is "+ str(newamount))


def main():
    Cardnumber = input("insert your card number:- ")
    pinnumber  = input("enter your pin number:- ")

    newuser =  Atm(Cardnumber ,pinnumber)

    print("Choose your activity")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        newuser.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
