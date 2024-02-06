import random
import string


letters = list(string.ascii_lowercase)
#returns list of alphabet
numbers = list(string.digits)
#return list of numbers in range (10)
special_char = list(string.punctuation)
#returns list of !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


def main():
    inputs()


def inputs():
    letter_count = int(input("How many letters in password? "))
    number_count = int(input("How many numbers in password? "))
    char_count = int(input("How many special characters in password? "))
    
    generate_password(letter_count, number_count, char_count)
    

def generate_password(letter_count, number_count, char_count):
    password = []
    
    for x in range(letter_count):
        password.append(random.choice(letters))
        
    for x in range(number_count):
        password.append(random.choice(numbers))
        
    for x in range(char_count):    
        password.append(random.choice(special_char))
     
    joined_password = "".join(password) 
    print(joined_password)

    

if __name__ == "__main__":
    main()