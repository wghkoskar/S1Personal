 name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
try:
   
    moneySaving = int(input("How much do you want to save a month (integer): "))
    integerTesting = moneySaving + 1
    totalMoney = moneySaving * 12
    print(f"Every year, you will save {totalMoney}")
    totalMoneyInterest = totalMoney * 1.008
    print(f"The money you will have saved in a year is £{totalMoneyInterest:.2f}")
except:
    print('Invalid Amount')

