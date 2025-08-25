class Bank:
    bankname="Statte Bank Of India"
    branch="A23 ,BBSR,India"

    def __init__(self,username,pancard,address):
        self.username=username
        self.pancard=pancard
        self.address=address
        self.balance=0.0
        print(f'Hiii{self.username} congrats! you are suceesfully created your account')

    def deposite(self,amount):
        self.balance=self.balance+amount
        print(f'you balnce amount is {self.balance}')
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print(f'you balnce amount is {self.balance}')

    def ministatement(self):
        print(f'your account balance is {self.balance}')

print(f'hello Welcome to the {Bank.bankname} from the  the branch of {Bank.branch}')
username=input('enter your username : ')
pancard=input('enter your pancard : ')
address=input('enter your address :')
b=Bank(username=username,pancard=pancard,address=address)


while True:
    print(f'select any options')
    print(f'1: Depoite\n2: Withdraw\n3:BalanceCheck\n4:Stop')
    option=int(input())
    if option==1:
        amount=float(input('plese enter your amount'))
        b.deposite(amount)
    elif option==2:
        amount=float(input('please enter your amount to withdraw'))
        b.withdraw(amount)
    elif option==3:
        print(f'the balance amount form your accout is {b.balance}')
        b.ministatement
    elif option==4:
        print(f'thanks for chossing {Bank.bankname}')
        break
    else:
        print('you enetered a  invalid option please select the valid option')