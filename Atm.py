class ATM:
    def __init__(self, card_number, pin):
        self.card_number=card_number
        self.pin=pin
    def CashWithdrawl(self, money_withdrawed):
        money_left=1000-money_withdrawed
        print("You have withdrawed: " + money_withdrawed+ "units")\
        print("You have "+ money_left + " left." )
    def BalanceInquiry(self):
        print("You have a starting balance of 1000 untis. Use it well.")

def start_operation():
    print("Card nunber:")
    card_number= input("Enter your card number here.")
    print("pin:")
    pin = input("Enter your pin here")
    account = ATM(card_number, pin)

    print("Hello. You can select which one you would like to do now:")
    print("1 - Balance Inquiry")
    print("2 - Withdrawing Cash")

    choice = int(input("Enter one of the numbers here: "))
    
    if(choice==1):
        account.BalanceInquiry()
    else:
        money_withdrawed = int(input("Enter the money you would like to withdraw from the account:"))
        account.CashWithdrawl(money_withdrawed)
