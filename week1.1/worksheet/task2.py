name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

try:
    moneySaving = int(input("How much do you want to save a month (integer): "))
    print(f"Every year, you will save {moneySaving * 12}")
    print(f"The money you will have saved in a year is £{(moneySaving * 12)* 1.008:.2f}")
except:
    print('Invalid Amount')

