import time 
print("WELCOME TO STATE BANK OF INDIA")
time.sleep(2)
#Starting the program
total_amount=664500.00    #assuming money in bank
pin=6750                  #Assuming pin of your ATM
code=str(input("Press * to continue="))
if(code=="*"):
    print("Please insert your card")
    time.sleep(1)
    print("Don't remove your card while processing")
    time.sleep(3)
    #Selecting language
    lan=str(input("Press 1 for ENGLISH and 2 for HINDI="))
    if (lan=="1"):
        print("Select operation you want")
        type=str(input("""Press # for NET BANKING \nPress ? for WITHDRAW MONEY \nPress & for CHECKING BANK BALANCE\nPress @ for ACTIVATING YOUR ATM \n*="""))     
        #Getting which type of operations you want
        if(type=="#"):
            print("Your NETBANKING is not activated ")
            time.sleep(2)                              #For activating netbanking
            activate= str(input("Press '!' to Activate"))
            print("Your NETBANKING is activted \n Now you can use our banking facility from just one click")   
       
        elif(type=="&"):
            print("Your current bank balance is=",total_amount,"Rupees")
        elif(type=="?"):
            pin=int(input("Please enter your 4 digit pin=")) #pin=6750
            if(pin==6750):
                print("Validating your Pin please wait") #validating pin
                time.sleep(3) 
                print("Your Pin is CORRECT")
                time.sleep(2)
                amount= float(input("Enter amount you want to withdraw=")) #amount withdraw
                time.sleep(2)
                if(amount>= total_amount):
                    print("OPPS! Your account does not having this much amount of money") #if withdraw amount is greater than your bank balance
                elif(amount<total_amount and amount>=20000):
                    print("You cannot withdraw money more than 200000 rupess at once") #money greater than 20000 but less than total amount
                elif(amount<20000):
                    print("Please wait Your cash is withdrawing") #cash withdrawing
            else :
                print("Your pin is INCORRECT")    
        elif(type=="@"):
            time.sleep(2)
            making=int(input("Create your 4 digit Pin=")) #creating pin
            time.sleep(1)
            print("Your ATM is activated")
        else:
             print("You have not selected the right operator")
    elif(lan=="2"):
        print("I am really verry sorry Right now i don,t know HINDI but i am learning")
else :
    print("You haven't choose '*'")  #operator choose
    print("Please Select right one")  
time.sleep(1)
print(""" Have a good day
    THANK YOU for using our ATM""") #the end
print("Please Visit again if needed")             






