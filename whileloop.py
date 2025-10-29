"""name= ""
while name!="stop":
    name= input("Enter your name (for end write stop)")
    print("Hello", name)"""
#User se password poochho,jab tak sahi password na likhe,
# tab tak program bar-bar pooche.
#Aur agar user 3 dafa galat likhe to —“Access Denied!” print ho jaaye

"""pasword= "python123"
attempt = 0
while attempt<3:
    user=input("Enter your password: ")
    if pasword == user:
        print("Your password is correct")
        break
    else:
        print("Try again")
    attempt=attempt+1
    if attempt==3:
        print("Access Denied! Too many wrong attempts")"""

#Computer ek secret number rakhega (maan lo 7).User ko us number ka guess karna hai.
#Agar user galat guess kare, program bole:
#“Too high!” ya “Too low!”

"""sec_num = 7
guess=0
attempt=0
while sec_num != guess and attempt<3:
    guess = int(input("Enter your guess number"))
    attempt=attempt+1
    if guess<sec_num:
        print("Too less, Try again")
    elif guess>sec_num:
        print("Too gigh Try again")
    if guess==sec_num:
        print("you're correct")
        break

    if attempt==3:
        print("you're exceeded")"""


#ATM simulator

"""User have 1000Rs
Program ask 4 statemnet
1, check balance
2.withdraw balance
3.deposit balance
4. exit, jb tk program exit nahi hota tb tk 4 stat chlti rahen"""

balance =1000

while True:
    print("---ATM machine")
    print("Press1 for checking balance")
    print("Press2 withdraw balance")
    print("Press3 Deposit balance")
    print("Press4 to Exit")
    user=int(input("Press 1-4..."))

    match user:
        case 1:
                print("your balance is ", balance)
        case 2:
              with_amo=int(input("Enter your withdraw amount"))
              if with_amo<=1000:
                balance -=balance
                print("You withdraw successfully your current bal is ", balance)
              else:
                   print("You don't have enough balance")
        case 3:
              dep_amo=int(input("Enter your Deposit amount"))
              balance +=dep_amo
              print("Succesfull, your cuurent balance is ", balance)
        case 4:
              print("Thank you for using ATM")
              break
        case _:
              print("Invalid, Please use number 1-4")