import re

def is_palindrome(string) -> bool:
    string = str(string).lower()
    string = re.sub(r'[^0-9a-z]','',string)
    reverse = string[::-1]
    return True if string == reverse else False

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal -- Panama"))
    print(is_palindrome("Madam, I'm Adam!"))
    print(is_palindrome(333))
    print(is_palindrome(None))
    print(is_palindrome("Abracadabra"))
