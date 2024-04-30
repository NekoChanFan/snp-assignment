import sys
import re

def is_palindrome(string):
    if not(isinstance(string,str)):
        return False
    string = string.lower()
    print(string)
    string = re.sub(r'[^0-9a-z]','',string)
    reverse = string[::-1]
    print(reverse)
    return True if string == reverse else False

def main():
    if(len(sys.argv) != 2):
        print("Wrong number of arguments")
        return
    print(is_palindrome(sys.argv[1]))

if __name__ == "__main__":
    main()
