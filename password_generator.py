import random
import string


letters = list(string.ascii_lowercase)
#returns list of alphabet
numbers = list(string.digits)
#return list of numbers in range (10)
special_char = list(string.punctuation)
#returns list of !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


def main():
    """
    Main function to run the password generator.
    """
    welcome()
    inputs()


def inputs():
    """
    Get user inputs for the number of letters, numbers, and special characters.
    """
    letter_count = int(input("How many letters in password? "))
    number_count = int(input("How many numbers in password? "))
    char_count = int(input("How many special characters in password? "))
    
    generate_password(letter_count, number_count, char_count)
    

def welcome():
    """
    Print a welcome message.
    """
    text = "Welcome to password generator!"
    split = "-" * len(text)
    print(text, split, sep="\n")
   
    

def generate_password(letter_count, number_count, char_count):
    """
    Generate a password based on user input counts.
    -----------------------------------------------
    Args:
        letter_count (int)
        number_count (int)
        char_count (int)
    """
    password_chars = []
    
    for x in range(letter_count):
        password_chars.append(random.choice(letters))
        
    for x in range(number_count):
        password_chars.append(random.choice(numbers))
        
    for x in range(char_count):    
        password_chars.append(random.choice(special_char))
     
    random.shuffle(password_chars)
    password = "".join(password_chars)
    print(f"Generated password: {password}")
    

if __name__ == "__main__":
    main()