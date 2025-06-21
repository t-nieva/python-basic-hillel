from curses.ascii import isalpha, isdigit


def is_palindrome(text):
    new_list = [item for item in text.lower() if isalpha(item) or isdigit(item)]
    if len(new_list) == 1:
        return True

    if new_list == new_list[::-1]:
        return True
    return False


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")
