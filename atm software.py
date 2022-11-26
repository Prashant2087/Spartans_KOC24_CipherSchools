# A python code to design an ATM machine
# Default Password is: 2087

print("_________________________________________________________________________________________________________________________________________\n")
print("                                                          WELCOME TO ATM Machine                                                           ")
print("_________________________________________________________________________________________________________________________________________\n")

pin=int(input("\nEnter the pin: "))
if pin==2087:
    bal=10000
    while True:   
        print("\n1- Credit amount")
        
        print("2- Withdraw amount")
        print("3- Customer Care")
        print("4- View Balance")
        print("0- Exit")
        choice=int(input("\nPlease select an option : "))
        if choice==0:
            break
        elif choice==1:
            user_deposit = int(input("\nEnter the amount you wish to deposit: ₹ "))
            bal+=user_deposit
            print(f"\nYou have deposited ₹{user_deposit} from your Account.")

        elif choice==3:                        
            print("\n-----Welcome To SBI Customer Care-----")
            print("\nTo check the details of your last 5 debit/credit transactions send an SMS 'MSTMT' to 09223866666 or give a missed call on the same number")
            print("\nFor quick support dial : 1800 425 3800")
            print("\nFor any product related enquiry and transaction related support please contact : ")
            print("Helpdesk : 022 - 27566066,022 - 27566067 (9.00am to 7.00 pm)")
            print("Fax : 022 - 27563478")
            print("Email : contactcentre@sbi.co.in")
            print("\nFor any other Help visit to nearest bank centre or login to  www.sbi.co.in ")


        elif choice==4:
            if bal<=5000:
                print("\nLow Balance")
            
            
            print(f"\nYour balance is: ₹{bal}")
        elif choice==2:
            
            user_withdraw = int(input("Enter the amount you wish to withdraw: ₹ "))
            if (bal-user_withdraw)>0:
                bal-=user_withdraw
                print('\n'+f"You have withdrawn ₹{user_withdraw} from your Account.")
            else:
                print("\nInsufficient Balance !!!")
               
        else:
            print("\nInvalid Option !!!!!")
            break
        inp=input("\nPress any key to continue")

    print("\n-------------------------------------THANKS FOR VISITING-------------------------------------")
else:
    print("\nInvalid pin !!!!")
    print("\nPlease Contact Customer Care")






    
