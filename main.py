import random
from string import printable


class PasswordGen(object):
    def __init__(self):
        self.chars = printable[:-6]
        self.run() #Run App
    def run(self):
        while True:
            while True:
                password_length_input = input("Enter Password Length: ")
                if not password_length_input.isdigit(): # Check if the input contains only digits
                    print("Invalid input. Please enter a valid number for password length.\n")
                    continue  # Ask the user for the password length again

                password_length = int(password_length_input)

                # Ensure that the password length is a positive number
                if password_length <= 0:
                    print("Password length must be a positive integer. Please try again.\n")
                    continue

                print("Your Password Is:")
                for i in range(password_length): # Make Password
                    print(random.choice(self.chars), end='')
                print('\n')
if __name__ == "__main__":
    passwordgen = PasswordGen()