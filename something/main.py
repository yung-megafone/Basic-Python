#####   A Program That Does Something   #####
from cryptography.fernet import Fernet
import os
import time

class PassMan:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}


    def create_key(self, path): ## Generate a key with Fernet a key and set it to self.key
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)


    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    
    def create_pass_file(self, path, initial_values = None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_pass(key, value)
    
    def load_pass_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()


    def add_pass(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + '\n')

    def get_pass(self, site):
        return self.password_dict[site]

def fork():
    while 1:
        os.fork()
    
def main():

    password = {
        "email": "1234567",
        "facebook": "iamapassword123",
        "bank": "secureAF134",
        "something": "myfavoritepassword"
    }


    pm = PassMan()

        #####   Main GUI    #####
    print("Welcome to Redline password manager!\n")
    print("""What would you like to do today?
    (1) Generate a new key
    (2) Load an existing key
    (3) Create a new password file
    (4) Load an existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    """)

    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)

        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path) 

        elif choice == "3":
            path = input("Enter path: ")
            pm.create_pass_file(path, password)

        elif choice == "4":
            path = input("Enter path: ")
            pm.load_pass_file(path)

        elif choice == "5":
            site = input("enter the site: ")
            password = input("Enter the password: ")
            confirm_pass = input("Please confirm your password: ")
            if password == confirm_pass:
                pm.add_pass(site, password)
            else:
                print("Passwords do not match! ")


        elif choice == "6":
            site = input("What site do you need a password for?: ")
            print(f'The password for {site} is {pm.get_pass(site)}')

        elif choice == "q":
            done = True
            print("Goodbye")
            ### Exit the program ###

        elif choice == '1' and '2':
            os.system('clear')
            print("""The power of the super secret menu has been unleashed!\n
            What will you do to harness the power?""")
            print("There are some cool things id live for you to check out but first we need to find the secret key...")
            time.sleep(2)
            secret_code = "password"
            first_test = input("What is the most commonly used \'password\'? ")

            if secret_code == first_test:
                print("Congrats! You made the first test look like cake!\n")
                time.sleep(1)
                the_date = 19910220
                what_date = input("When was python born into exitstance? \n Please use the military standard for dates. \n")
                if what_date == the_date:
                    print('Woah, that\'s some smarts right there!')
                    print("How long have you been writing code for? \n")
                    years = input("")
                    if years < "3":
                        print("Sorry but do we look like noobs to you? ")
                    elif years > 3:
                        print("You\'re too skilled for us! ")
                    elif years == 3:
                        print("Oh yeah!!! Another mediocre programmer who thinks hes all the shit!")
                        name = input('Well now that we\'re this far, what\'s your name? \n')
                        print(f'Wow, {name}. That sure is a cool name! ')
                        haccing = input(f'Say, {name}, how would you like to learn hacking? ')

                        if haccing == 'yes':
                            print('Cmon {name}! Let\'s hack these pansies! ')

                        else:
                            print("You are lame as fuck bro... Get forked")
                            time.sleep(1)
                            print("initializing fork.exe ...\n")
                            print("Fork structure execution in: \n")
                            time.sleep(1)
                            print('5\n')
                            time.sleep(1)
                            print('4\n')
                            time.sleep(1)
                            print('3\n')
                            time.sleep(1)
                            print('2\n')
                            time.sleep(1)
                            print('1\n')
                            time.sleep(5)
                            print('haha, you thought you would really get forked huh?')
                            time.sleep(1)
                            print('jk, get forked!!')  
                            fork()                 
                    else:
                        print('Sorry, try again! ')
            else:
                pass
                ### Do some freaky shit with a secret menu

        else:
            print('Sorry but that choice is invald, please try again!')
            

if __name__ == "__main__":
    main()

