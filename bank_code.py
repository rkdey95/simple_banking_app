#NAME: RUPESH KUMAR DEY
#ID  : TP061720

# Program defined username and password for Admin account. Only one Admin username and Password defined.
ad_user_pass = ["Admin","Adminbank123"]

#To be used later in the program to get current date and time to be used in displaying information and to name files
from datetime import datetime

#FUNCTIONS TO BE USED IN THE PROGRAM SECTION
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION 1
#The function that displays the welcome page to the bank. User has 3 options to either login as 1) Admin, 2) Customer or 3) exit the program through a menu display
#User to either enter 1,2 or 3 only.
#Validation is done to ensure that until customer enters either one of the 3 digit options. If other integers are entered, a pop up error is shown and the program will loop until the correct value is entered.
#DO NOT ENTER A STRING VALUE AS THE. THIS WILL CAUSE THE PROGRAM TO FAIL DUE TO ERROR OF DATA TYPE.
#the program will return the user_type
def welcome_page():
    print("\n")
    print("Hello there! Good day. Welcome to Rupesh's Bank")
    user_type = str(input("Please let us know if you're a Customer or Admin\n1. Admin \n2. Customer \n3. Exit program\n"))
    while is_int(user_type) == False:
        user_type = str(input("Input Error. Please enter only numbers 1, 2 or 3:\n"))
    user_type = int(user_type)
    #while (user_type.isalnum() == True or user_type.isalpha() == True) and user_type.isnumeric() == False :
    #    user_type = str(input("Input Error. Please enter only numbers 1, 2 or 3. Please let us know if you're a Customer or Admin\n1. Admin \n2. Customer \n3. Exit program\n"))
    user_type = int(user_type)
    while (user_type !=1 and user_type!=2 and user_type!=3):
        print("User type is invalid. Please try again. Please only enter either value 1 or 2 or 3")
        user_type = int(input("\nPlease let us know if you're a Customer or Admin\n1. Admin \n2. Customer \n3. Exit program\n"))
    return user_type

#FUNCTION 1A - Function that checks if the input is an integer or not. If input is integer, the program returns a True boolean. Else False boolean is returned.
def is_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
#FUNCTION 1B - Function that checks if the input is a float or not. If input is float, the program returns a True boolean. Else False boolean is returned.
def is_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

#FUNCTION 2
# This function is used to create a customer profile by Admin.
def create_cust_profile():
    # prompting message once Admin chooses to create a customer account. Informing user that there is an option to enter 000000 to quit program if they want to
    print("Let's create customer profile. To exit at any point just type 000000 for any section\n")

    #Entering customer details. Name, ID, account number, citizenship, assigned username and password.
    ad_add_name = str(input("Please input customer's name:\n"))
    while ad_add_name == "":
        ad_add_name = str(input("Error! No input given. Please input customer's name:\n"))
    stop_program(ad_add_name)

    ad_add_id = str(input("Please input customer's ID:\n"))
    while ad_add_id == "":
        ad_add_id = str(input("Error! No input given. Please input customer's ID:\n"))
    stop_program(ad_add_id)

    ad_add_account = str(input("Please input customer's account number:\n"))
    while ad_add_account == "":
        ad_add_account = str(input("Error! No input given. Please input customer's account number:\n"))
    while is_int(ad_add_account) == False:
        ad_add_account = str(input("Input Error. Please enter only numerical values:\n"))
    ad_add_account = int(ad_add_account)
    #validation step to ensure that customer account number does not already exist in the bank. If it does then an error message will be prompted and program will loop until
    #a new account number is entered.
    while ad_add_account in (item for sublist in customer_list for item in sublist):
        ad_add_account = str(input("Customer account number already exists. Please input another customer's account number or press 000000 to exit program:\n"))
        while ad_add_account == "":
            ad_add_account = str(input("Error! No input given. Please input customer's account number:\n"))
        ad_add_account = int(ad_add_account)
        stop_program(ad_add_account)
    stop_program(ad_add_account)

    ad_add_citizenship = str(input("Please input customer's citizenship:\n"))
    while ad_add_citizenship == "":
        ad_add_citizenship = str(input("Error! No input given. Please input customer's citizenship:\n"))
    stop_program(ad_add_citizenship)

    ad_add_user = str(input("Please input customer's username:\n"))
    while ad_add_user == "":
        ad_add_user = str(input("Error! No input given. Please input customer's username:\n"))
    stop_program(ad_add_user)

    ad_add_pass = str(input("Please input customer's password:\n"))
    while ad_add_pass == "":
        ad_add_pass = str(input("Error! No input given. Please input customer's password:\n"))
    stop_program(ad_add_pass)
    # array to store customer transaction history in the form of array [["Deposit",65.63],["Withdrawal"],25.54],...]
    transactions = []
    # account total initially is 0
    account_total = 0.00

    #returns an array with all the parameters.
    return [ad_add_name,ad_add_id,ad_add_account,ad_add_citizenship,ad_add_user,ad_add_pass,transactions,account_total]

#FUNCTION 3
#Function to exit program
#before exiting program all txt files in the folder will be archieved into a zip file.
#Customer list will be cleared once program is terminated.
def stop_program(input):
    if input == 000000 or input == 0.0:
        input = "000000"
    if input == "000000":
        zip_file()
        quit()

#FUNCTION 4
#Function to archieve all txt files in the folder once the program is ended.
#List of customers will also be written into the txt file and archieved into the zip file
#the format name for the zip file will be presented as such:
#File_created--DD_MM_YYYY--HH_MM_SS
def zip_file():
    import zipfile, os
    from os import path
    today = datetime.now().strftime("File_created--%d_%m_%Y--%H_%M_%S")
    handle_customer_list = open('Customer List_' + today + '.txt', 'w')
    for x in customer_list:
        handle_customer_list.write(str(customer_list.index(x)+1) + ' ------\t' + str(x) + '\n')
    handle_customer_list.close()
    filename = str(today + '.zip')
    fh = zipfile.ZipFile(filename, 'w')
    for x in os.listdir():
        if x.endswith('.txt'):
            fh.write(x, compress_type=zipfile.ZIP_DEFLATED)
    fh.close()
    directory = path.abspath(path.curdir)
    for x in os.listdir(directory):
        if x.endswith('.txt'):
            os.unlink(directory + '//' + x)

#FUNCTION 5
#Creates a txt file with a history of customers transaction.
#the txt file is overwritten each time the customer performs a new transaction or each time the function is called.
#the file name will be saved in the format of the customer's account number.
def create_file(arr):
    filename = str(arr[2]) + '.txt'
    account_number = str(arr[2])
    fh = open(filename,'w')
    fh.write("Customer Name           : %s" %arr[0])
    fh.write("\nCustomer ID             : %s" %arr[1])
    fh.write("\nCustomer Account Number : %d"%arr[2])
    fh.write("\n\n")
    fh.write("No     Transaction Type            Transaction Date            Transaction Amount\n")
    fh.write("--     ----------------            ----------------            ------------------\n")
    counter = 1
    for xx in arr[6]:
        fh.write("%d      "%counter)
        fh.write(xx[0]+"                  ")
        fh.write(xx[1]+"                  ")
        fh.write("%.2f\n"%xx[2])
        counter = counter + 1
    fh.write("\nCurrent Account Balance: %.2f\n"%arr[7])
    fh.close()

#FUNCTION 6
#This function reads the customer's txt file when Admin  chooses to view csutomer transaction history.
def read_file(acc_num):
    filename = str(acc_num)+'.txt'
    fh = open(filename,'r')
    print (fh.read())
    fh.close()

#TESTER used for testing the program's functionality
#customer_list = [['Rupesh Kent', '123456', 654321, 'Malaysian', 'rkent', '654321', [], 0],
#['Lex Luthor', '134679', 976431, 'Malaysian', 'bkdey', '976431', [], 0],
#['Johnathan Kent', '853366123056', 7414789, 'American', 'john85', 'superman', [], 0.0],
#['Clark Kent', '665544', 665544, 'Kryptonian', 'super', 'batman', [['Deposit   ', '03/08/2020', 200.35], ['Deposit   ', '03/08/2020', 200.35], ['Withdrawal', '03/08/2020', 20.25]], 380.45]]

#Initializing customer list as an empty array.
customer_list = []

#looping variable used to loop the program to return to main menu page or go back to Admin login / Customer login page
back_to_menu = True
back_to_admin = True
while back_to_menu == True or back_to_admin == True:
    #Displaying Welcome page
    user = welcome_page()

#ADMIN SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------
    #If user type selected is Admin
    if user == 1:

        #program will request Admin to choose to either login to their account or go back to main menu
        ad_login = str(input("\nPlease choose either option to: \n1. Login to Admin Account\n2. Go back to main menu\n"))
        while is_int(ad_login) == False:
            ad_login = str(input("Input Error. Please enter only numbers 1 or 2:\n"))
        ad_login = int(ad_login)


        #Validation to ensure that only either option 1 or 2 is selected. Else the program will loop this section until correct input is entered.
        while ad_login != 1 and ad_login != 2:
            print("\nAction type is invalid. Please try again. Please only enter either value 1 or 2")
            ad_login = int(input("\nPlease choose either option to: \n1. Login to Admin Account\n2. Go back to main menu\n"))

        #if Admin selects option 2 the program will return to main menu
        if ad_login == 2:
            continue

        #Admin logging in page. Where admin will need to input their username and password
        #validation is done to ensure that correct username and password is entered.
        #Option is given to enter 000000 to exit program by calling stop_program function
        else:
            back_to_menu = False
            ad_user = ""
            ad_pass = ""
            ad_user = str(input("\nPlease input username:\n"))
            ad_pass = str(input("Please input password:\n"))
            while (ad_user != ad_user_pass[0] or ad_pass != ad_user_pass[1]):
                stop_program(ad_user)
                stop_program(ad_pass)
                print("Admin Username or password is incorrect. Please try again. Else press 000000 to exit program")
                ad_user = str(input("\nPlease input username:\n"))
                ad_pass = str(input("Please input password:\n"))
            print("Login Success!\n")

            #Looping variable to loop back to Admin operation menu page each time unless option to return to main menu page is selected.
            back_to_admin = False
            while back_to_admin == False:


                #Once Login is successful, admin can choose to either 1) Create Customer Account, 2) View Customer Profile, 3) View Customer Transaction and 4) Go back to Main Menu
                #Validation is done to ensure that valid input 1,2,3 or 4 is entered.
                admin_ops = str(input("Please choose either option to: \n1. Create Customer Account\n2. View Customer Profile\n3. View Customer Transaction\n4. Go back to Main Menu\n"))
                while is_int(admin_ops) == False:
                    admin_ops = str(input("Input Error. Please enter only numbers 1, 2, 3 or 4:\n"))
                admin_ops = int(admin_ops)
                while admin_ops != 1 and admin_ops != 2 and admin_ops != 3 and admin_ops != 4:
                    print("\nAction type is invalid. Please try again. Please only enter either value 1 or 2 or 3")
                    admin_ops = int(input("Please choose either option to: \n1. Create Customer Account\n2. View Customer Profile\n3. View Customer Transaction\n4. Go back to Main Menu\n"))

                #If admin chooses to CREATE CUSTOMER PROFILE
                #The create_cust_profile function will be called and the customer details will be added to the customer_list array
                #create_file function will also be called to produce a blank txt file with no transaction history with customer details to be updated later on.
                if admin_ops == 1:
                    profile = create_cust_profile()
                    customer_list.append(profile)
                    create_file(profile)
                    print("\nCustomer profile successfully created!\nNext Transaction\n")

                #If admin chooses to VIEW CUSTOMER PROFILE
                #-----------------------------------------------------------------------------------------------------------------------------
                #Admin will need to input customer's number
                elif admin_ops == 2:

                    #Looping variable to user to loop the while loop until correct customer account number is entered.
                    back_to_view = True

                    #Loop until an account number that exists in the customer_list is entered.
                    while back_to_view == True:
                        ad_customer_account = int(input("\nPlease input customer's account number:\n"))
                        for x in customer_list:
                            #matching the customer account number to the particular customer in the customer_list
                            if ad_customer_account == x[2]:
                                print("\n")
                                print("Customer's Details")
                                print("===============================================================================")
                                print("Customer's name        :", x[0])
                                print("Customer's ID          :", x[1])
                                print("Assigned account number:", x[2])
                                print("Customer's Citizenship :", x[3])
                                print("Customer's Username    :", x[4])
                                print("Password               :", x[5])
                                print("\n")
                                back_to_view = False

                        #If customer_list is empty, then there is no customer. the progam will return to Admin Menu page.
                        if customer_list == []:
                            print("There is no customer at the moment. Please create new customer first\n")
                            back_to_view = False
                            continue

                        #if customer account number does not match any account number in customer list, and error message will pop up prompting admin to input correct account number.
                        #if customer enters 000000 the program will exit.
                        if back_to_view == True:
                            stop_program(ad_customer_account)
                            print("\nI am sorry. Customer doesn't exist. Please check details again or create customer profile\nOr enter 000000 to exit")
                            continue

                # If admin chooses to VIEW CUSTOMER TRANSACTION
                # -----------------------------------------------------------------------------------------------------------------------------
                elif admin_ops == 3:

                    # Loop until an account number that exists in the customer_list is entered.
                    back_to_view = True
                    while back_to_view == True:
                        ad_customer_account = int(input("\nPlease input customer's account number:\n"))

                        #Finds the customer txt file. Reads the customer details within and displays it.
                        for x in customer_list:
                            if ad_customer_account == x[2]:
                                print("\n")
                                read_file(ad_customer_account)
                                back_to_view = False

                        #If there is no customer in the customer_list, then the program will return back to admin menu page.
                        if customer_list == []:
                            print("There is no customer at the moment. Please create new customer first\n")
                            back_to_view = False
                            continue

                        # if customer account number does not match any account number in customer list, and error message will pop up prompting admin to input correct account number.
                        # if customer enters 000000 the program will exit.
                        if back_to_view == True:
                            stop_program(ad_customer_account)
                            print("\nCustomer doesn't exist. Please check details again or create customer profile\nOr enter 000000 to exit")
                            continue

                #If option to return to main menu is chosen, then the program will return to admin menu page
                else:
                    back_to_admin = True

    #================================================================================================================================================================
    #CUSTOMER SECTION

    elif user == 2:

        #If customer_list is empty, then error message will show up indicating that you do not have an account with the bank. The program will return to main menu page.
        if customer_list == []:
            print("You do not have an account with Rupesh's Bank. Please sign up\n")
            continue

        #Else user will be given option to either 1) Login into account or 2) Go back to main menu
        else:
            cust_login = str(input("\nPlease choose either option to: \n1. Login to Your Account\n2. Go back to main menu\n"))
            while is_int(cust_login) == False:
                cust_login = str(input("Input Error. Please enter only numbers 1 or 2:\n"))
            cust_login = int(cust_login)

            #Validation step. If other options besides 1 and 2 are selected then the program will loop this while section until a correct input is entered.
            while cust_login != 1 and cust_login != 2:
                print("\nAction type is invalid. Please try again. Please only enter either value 1 or 2")
                cust_login = int(input("Please choose either option to: \n1. Login to Your Account\n2. Go back to main menu\n"))

            #When customer chooses to return to main menu
            if cust_login == 2:
                continue

            #Customer Login Page
            else:

                #looping variable to decide whether to return to main menu page or not.
                back_to_menu = False

                #getting customer input on username and password
                cust_user = str(input("\nPlease input username:\n"))
                cust_pass = str(input("Please input password:\n"))

                #Searching customer username and password to the values inside customer_list
                for x in customer_list:

                    #if customer exists but password is wrong. The program will loop until correct password is entered. Customer is also given option to exit program by entering 0000000
                    if cust_user == x[4]:
                        while cust_pass != x[5]:
                            stop_program(cust_pass)
                            cust_pass = str(input("Wrong password. Please try again. Or press 000000 to exit to main menu:\nPassword: "))
                        print("Login Successful!")
                        back_to_menu = True

                #If customer account doesnt exist in the customer_list Error message will pop up and program will return to main menu page.
                if back_to_menu == False:
                    print("You do not have an account with Rupesh's Bank. Please sign up\n")
                    back_to_menu = True
                    continue


                #Looping variable to loop back to customer operation menu page
                back_to_view = True
                while back_to_view == True:

                    #Customer Menu operation page
                    #customer is required to enter either option 1) Perform deposit, 2) Perform withdrawal, 3) View transaction Histroy and 4) Return to main menu
                    cust_ops = str(input("\nPlease choose either option to: \n1. Perform Deposit\n2. Perform Withdrawal\n3. View your Transaction History\n4. Go back to Main Menu\n"))
                    while is_int(cust_ops) == False:
                        cust_ops = str(input("Input Error. Please enter only numbers 1, 2, 3 or 4:\n"))
                    cust_ops = int(cust_ops)

                    #validation step to ensure that valid input is entered else the program will loop
                    while cust_ops != 1 and cust_ops !=2 and cust_ops !=3 and cust_ops !=4:
                        cust_ops = int(input("\nAction is invalid. Please try again. Please choose either option to: \n1. Perform Deposit\n2. Perform Withdrawal\n3. View your Transaction History\n4. Go back to Main Menu\n"))

                    #If customer chooses to DEPOSIT. Deposit amount is float rounded off to 2 decimal places.
                    if cust_ops == 1:
                        cust_deposit = str(input("\nPlease input deposit amount:\nDeposit Amount: "))
                        while is_float(cust_deposit) == False:
                            cust_deposit = str(input("Input Error. Please enter a value with 2 decimal places:\nDeposit Amount: "))
                        cust_deposit = round(float(cust_deposit),2)

                        #If deposit amount is 0 or lesser, error message will pop up asking customer to enter valid amount. If 000000 is entered the program will exit.
                        while cust_deposit <= 0:
                            stop_program(cust_deposit)
                            cust_deposit = str(input("\nInvalid deposit amount. Please try again or press 000000 to exit program\nDeposit Amount: "))
                            while is_float(cust_deposit) == False:
                                cust_deposit = str(input("Input Error. Please enter a value with 2 decimal places:\nDeposit Amount: "))
                            cust_deposit = round(float(cust_deposit), 2)

                        #Once valid deposit amount is entered. The customer username is matched to the one in customer_list. If the customer exists then the transaction array in the customer_list will be updated with
                        #with an ["Deposit",xx.xx amount] array. The txt file of the particular customer will also be updated by overwritting the txt file.
                        #Customer's total account balance in the customer list will be updated to add the deposit amount. This will also be updated in the txt file.
                        for x in customer_list:
                            if cust_user == x[4]:
                                today = datetime.now().strftime("%d/%m/%Y")
                                x[6].append(["Deposit   ", today, round(cust_deposit,2)])
                                x[7] = round(x[7] + cust_deposit,2)
                                create_file(x)
                                print("Deposit Successful\n\n")

                    # If customer chooses to WITHDRAW. Withdraw is stored as a float rounded to 2 decimal places.
                    elif cust_ops == 2:
                        for x in customer_list:
                            if cust_user == x[4]:
                                customer_total = x[7]

                        #If customer account balance is zero. Then program will return to customer menu page. Customer has to deposit money first before withdrawal can be done.
                        if customer_total == 0:
                            print("\nYour bank account balance is 0. Please deposit some money first\n")
                            continue

                        #Asking user for withdrawal amount in the form of float rounded to two decimal places.
                        else:
                            cust_withdraw = str(input("\nPlease input withdrawal amount:\nWithdrawal Amount: "))
                            while is_float(cust_withdraw) == False:
                                cust_withdraw = str(input("Input Error. Please enter a value with 2 decimal places:\nWithdrawal Amount: "))
                            cust_withdraw = round(float(cust_withdraw), 2)

                            #If customer withdrawal amount is more than customer bank total bank account balance.
                            #Error message will pop up asking user to enter a lesser amount. Customer can enter 000000 to exit program.
                            while cust_withdraw > customer_total:
                                stop_program(cust_withdraw)
                                print("\nWithdrawal amount more than account balance. please try again or press 000000 to exit program")
                                cust_withdraw = str(input("\nPlease input withdrawal amount:\nWithdrawal Amount: "))
                                while is_float(cust_withdraw) == False:
                                    cust_withdraw = str(input("Input Error. Please enter a value with 2 decimal places:\nWithdrawal Amount: "))
                                cust_withdraw = round(float(cust_withdraw), 2)

                            # If withdrawal amount is 0 or lesser, error message will pop up asking customer to enter valid amount. If 000000 is entered the program will exit.
                            while cust_withdraw <= 0:
                                stop_program(cust_withdraw)
                                cust_withdraw = str(input("\nInput Error. Withdrawal amount invalid. Please input correct withdrawal amount or enter 000000 to exit program:\nWithdrawal Amount: "))
                                while is_float(cust_withdraw) == False:
                                    cust_withdraw = str(input("Input Error. Please enter a value with 2 decimal places:\nWithdrawal Amount: "))
                                cust_withdraw = round(float(cust_withdraw), 2)

                            # Once valid withdrawal amount is entered. The customer username is matched to the one in customer_list. If the customer exists then the transaction array in the customer_list will be updated with
                            # with an ["Withdrawal",xx.xx amount] array. The txt file of the particular customer will also be updated by overwritting the txt file.
                            #Customer's total account balance in the customer list will be updated to deduct the withdrawal amount. This will also be updated in the txt file.
                            for x in customer_list:
                                if cust_user == x[4]:
                                    today = datetime.now().strftime("%d/%m/%Y")
                                    x[6].append(["Withdrawal", today, round(cust_withdraw, 2)])
                                    x[7] = round(x[7] - cust_withdraw, 2)
                                    create_file(x)
                                    print("Withdrawal Successful\n")

                    #If Option 3 is selected, the customer's entire transaction history up to date will displayed. Data is obtained from the customer_list array.
                    elif cust_ops == 3:
                        print("\n")
                        print("No     Transaction Type            Transaction Date            Transaction Amount")
                        print("--     ----------------            ----------------            ------------------")
                        counter = 1
                        for x in customer_list:
                            if cust_user == x[4]:
                                for xx in x[6]:
                                    print(counter, "     ", xx[0], "               ", xx[1], "                ", round(xx[2],2))
                                    counter = counter + 1
                                print("\nCurrent Account Balance: ", round(x[7],2), "\n")

                            #txt file is also updated
                            create_file(x)

                    #If customer chooses to return back to main menu page.
                    else:
                        back_to_menu = True
                        back_to_view = False
                        continue

#=========================================================================================================================================
#EXIT PROGRAM
    else:
        #Creates an archieve zip file and exits the program.
        zip_file()
        print("Thank you for Banking with us. We hope to see you again. :)")
        quit()

















