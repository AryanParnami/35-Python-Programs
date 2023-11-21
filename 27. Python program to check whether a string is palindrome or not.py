def is_palindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
    return s == s[::-1]

# Example usage
string_input = input("Enter a string: ")
if is_palindrome(string_input):
    print(f"{string_input} is a palindrome.")
else:
    print(f"{string_input} is not a palindrome.")
