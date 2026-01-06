# i = 1 
# while(i <= 10):
#     print(i)
#     i += 1

# bank app
# ask user for w (withdraw), d (deposit), c (check balance), e (exit)
# initial balance is 0
# if choose d ask for amount
# if choose w ask for amount
# if choose c show balance
# if choose e exit/terminate
 
def bankApp() :
    balance = 0
 
    while 1:
        print("------------------------------------------------")
        print("d / D (Deposit)")
        print("w / W (Withdraw)")
        print("c / C (Check balance)")
        print("e / E (Exit)")
        ope = str(input("Enter a operation D, W, C, E: "))
 
        if ope == "d" or ope == "D":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Amount deposited successfully.")
        
        elif ope == "w" or ope == "W":
            if balance == 0:
                print("Make a deposit first. Your current balance is 0. ")
            else :
                amount = int(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance.")
                else :
                    balance -= amount
                    print("Amount withdrawed sccessfully.")
        
        elif ope == "c" or ope == "C":
            if balance == 0:
                print("Make a deposit first. Your current balance is 0. ")
            else :
                print("Your current balance: ")
                print(balance)
            
        elif ope == "e" or ope == "E":
            if balance == 0:
                print("Make a deposit first. Your current balance is 0. ")
            else:
                break
        
        else :
            print("Invalid operation. Enter a valid operaiton.")
 
bankApp()