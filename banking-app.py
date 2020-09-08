#Banking App

#Sample Users
bank_data = {'test':{'pin':12, 'amount':5555555,'place':'City 1'}, 'test1':{'pin':123, 'amount':45454545,'place':'City 2'}}

#Function to go back to main menu
def back_to_main():
    input('\nPress Enter to go back to Main Menu... ')
    
print('''
================================================
----------  Welcome to New Leaf Bank  ----------
================================================''')
while True :
    print('''
----------------- Main Menu ---------------------

        1.  Open New Account
        2.  Withdraw
        3.  Deposit
        4.  View Customer Details
        5.  Check Account Balance
        6.  Quit

-------------------------------------------------''')

    choice = input('Enter Choice : ')
    print('-------------------------------------------------')
    
    if choice == '1':
        print()
        name = input('Enter Name  : ')
        if name in bank_data:
            print("\nUser '",name,"' Already Exist\n")
            
            back_to_main()
        else:
            
            pin = int(input('Enter Pin : '))
            print('\n Note : Do Not Forget NAME & PIN...\n')
            place = input('Enter City of Origin    : ')
            amt = int(input('Enter Amount to Deposit : '))
            
            
            user_data = {}

            user_data['pin'] = pin
            user_data['place'] = place
            user_data['amount'] = amt
            
            bank_data[name] = user_data
            back_to_main()

    elif choice == '2':
        print()
        usn = input('Enter Valid User Name : ')
        
        if usn in bank_data:
            pin = int(input('Enter Pin    : '))
            pinbank = bank_data[usn]['pin']
            
            #Verificatio of pin
            if pin == pinbank:
                amt = int(input('Enter Amount To Withdraw : '))
                #Check for Sufficient Balance
                if amt > bank_data[usn]['amount']:
                    print('\nInsufficient Balance.')
                else :
                    bank_data[usn]['amount'] = bank_data[usn]['amount'] - amt
                    print('\nRs.',amt,'/- debited from your account.')
                    print('Your Final Balance is Rs.', bank_data[usn]['amount'],'/-')
                
                back_to_main()
            else :
                print('\nIncorrect PIN')
                
                back_to_main()
        else :
            print("\n User '",usn,"' does not exist.")
            
            back_to_main()

    elif choice == '3':
        print()
        usn = input('Enter Valid Username : ')
        
        if usn in bank_data:
            pin = int(input('Enter Pin    : '))
            pinbank = bank_data[usn]['pin']
            
            #Verification of pin
            if pin == pinbank:
                amt = int(input('Enter Amount To Deposit : '))
                bank_data[usn]['amount'] = bank_data[usn]['amount'] + amt
                print('\nRs.',amt,'/- credited to your account.')
                print('Your Final Balance is Rs.', bank_data[usn]['amount'],'/-')
                
                back_to_main()
            else :
                print('\nIncorrect PIN')
                
                back_to_main()
        else :
            print("\n User '",usn,"' does not exist.")
            
            back_to_main()
            
    elif choice =='4':
        #Print Data of Customers an their Places
        print()
        print('Total Customers : ',len(bank_data))
        print()
        print ("{:<20}  {:<15}".format('Name', 'Place'))
        print('---------------------------------------------')
            
        for name in bank_data:
            place = str(bank_data[name]['place'])
            #First Letter Capitalization
            name1 = name[0].upper()
            name = name1+name[1:]
            place1 = place[0].upper()
            place = place1+place[1:]
            print ("{:<20}  {:<15}".format(name, place))
        
        back_to_main()
    
    elif choice == '5':
        #Print Data of Customers and Balances
        print('''
        1. All Customer Account Balance
        2. Specific Customer Account Balance
-------------------------------------------------''')
        ch = int(input('Enter Choice : '))
        print()
        
        if ch == 1:
            print ("{:<20}  {:<15}".format('Name', 'Balance'))
            print('------------------------------------------')
            
            for name in bank_data:
                amount = 'Rs.'+ str(bank_data[name]['amount']) + '/-'
                #First Letter Captitalization
                name1 = name[0].upper()
                name = name1+name[1:]
                print ("{:<20}  {:<15}".format(name, amount))
                

            back_to_main()

        elif ch == 2:
            usn = input('Enter Customer Name : ')
            
            if usn in bank_data:
                print('Your Account Balance is Rs.',bank_data[usn]['amount'],'/-')
                
                back_to_main()
            else:
                print("User '",usn,"'does not exist.")
                
                back_to_main()
        else:
            print('\nInvalid Option.')
            
            back_to_main()

    elif choice == '6':
        print('\n**** Thank You For Banking With Us. *****\n')
        break
    else:
        print('\nInvalid Option.')

        back_to_main()
