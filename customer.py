class Customer:

    def __init__(self, email):
        self.__last_name = ""
        self.__first_name = ""
        self.__age = 0
        self.__email = email
        self.__password = ""
        self.__card_number = ""
        self.__security_code = ""

    def input_age(self):
        self.__age = input("Enter age:")
        while self.__age.isdigit() == False:
            print("Error: Age must be an integer.")
            self.__age = input("Enter age:")

    def input_password(self):
        print("Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number.")
        self.__password = str(input("Enter password:"))
        if (any(x.isupper() for x in self.__password) and any(x.islower() for x in self.__password)
        and any(x.isdigit() for x in self.__password) and len(self.__password) < 8 and len(self.__password) > 12):
            print("Incorrect format. Please Re-enter.")
            self.__password = str(input("Enter password."))


    def input_card_number(self):
        self.__card_number = str(input("Enter 16-digit credit card number:"))
        while len(self.__card_number) < 16 or len(self.__card_number) > 16 or self.__card_number.isalpha() == True:
            print("Card number must be 16 digits.")
            self.__card_number = str(input("Enter 16-digit credit card number:"))

    def input_security_code(self):
        self.__security_code = str(input("Enter 3 digit security code:"))
        while len(self.__security_code) < 3 or len(self.__security_code) > 3 or self.__security_code.isalpha() == True:
            print("Security number must be 3 digits.")
            self.__security_code = str(input("Enter 3 digit security code:"))

    def input_info(self):
        self.__first_name = str(input("First name:"))
        self.__last_name = str(input("Last name:"))
        Customer.input_age(self)
        Customer.input_password(self)
        Customer.input_card_number(self)
        Customer.input_security_code(self)

    def verify_info(self):
        print("\n1. First name:",self.__first_name)
        print("2. Last name:",self.__last_name)
        print("3. Email address:",self.__email)
        print("4. Password:",self.__password)
        print("5. Age:",self.__age)
        print("6. Card number:",self.__card_number)
        print("7. Security code:",self.__security_code)
        choice = int(input("\nTo correct any entry, enter the entry's number and press RETURN. If everything is correct, press 0:"))
        while choice != 0:
            if choice == 1:
                self.__first_name = str(input("First name"))
                print("\n1. First name:",self.__first_name)
                print("2. Last name:",self.__last_name)
                print("3. Email address:",self.__email)
                print("4. Password:",self.__password)
                print("5. Age:",self.__age)
                print("6. Card number:",self.__card_number)
                print("7. Security code:",self.__security_code)
            elif choice == 2:
                self.__last_name = str(input("Last name:"))
                print("\n1. First name:",self.__first_name)
                print("2. Last name:",self.__last_name)
                print("3. Email address:",self.__email)
                print("4. Password:",self.__password)
                print("5. Age:",self.__age)
                print("6. Card number:",self.__card_number)
                print("7. Security code:",self.__security_code)
            elif choice == 3:
                self.__email = str(input("Email address:"))
                print("\n1. First name:",self.__first_name)
                print("2. Last name:",self.__last_name)
                print("3. Email address:",self.__email)
                print("4. Password:",self.__password)
                print("5. Age:",self.__age)
                print("6. Card number:",self.__card_number)
                print("7. Security code:",self.__security_code)
            elif choice == 4:
                Customer.input_password(self)
                print("\n1. First name:",self.__first_name)
                print("2. Last name:",self.__last_name)
                print("3. Email address:",self.__email)
                print("4. Password:",self.__password)
                print("5. Age:",self.__age)
                print("6. Card number:",self.__card_number)
                print("7. Security code:",self.__security_code)
            elif choice == 5:
                Customer.input_age(self)
                print("\n1. First name:",self.__first_name)
                print("2. Last name:",self.__last_name)
                print("3. Email address:",self.__email)
                print("4. Password:",self.__password)
                print("5. Age:",self.__age)
                print("6. Card number:",self.__card_number)
                print("7. Security code:",self.__security_code)
            elif choice == 6:
                Customer.input_card_number(self)
                print("\n1. First name:",self.__first_name)
                print("2. Last name:",self.__last_name)
                print("3. Email address:",self.__email)
                print("4. Password:",self.__password)
                print("5. Age:",self.__age)
                print("6. Card number:",self.__card_number)
                print("7. Security code:",self.__security_code)
            elif choice == 7:
                Customer.input_security_code(self)
                print("\n1. First name:",self.__first_name)
                print("2. Last name:",self.__last_name)
                print("3. Email address:",self.__email)
                print("4. Password:",self.__password)
                print("5. Age:",self.__age)
                print("6. Card number:",self.__card_number)
                print("7. Security code:",self.__security_code)
        print("Registration and Verification completed for this customer.")

    def output_info(self):
        f = open("customers.txt","w")
        for i in range(10):
            f.write(self.__first_name)
            f.write("\n")
            f.write(self.__last_name)
            f.write("\n")
            f.write(self.__age)
            f.write("\n")
            f.write(self.__email)
            f.write("\n")
            f.write(self.__password)
            f.write("\n")
            f.write(self.__card_number)
            f.write("\n")
            f.write(self.__security_code)
            i+=1
        f.close()
