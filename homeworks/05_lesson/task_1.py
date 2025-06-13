import keyword
import string


def validate_variable(variable_name: str) -> bool:
    if variable_name[0].isdigit():
        return False

    if keyword.iskeyword(variable_name):
        return False

    if 1 < len(variable_name) == variable_name.count("_"):
        return False

    for letter in variable_name:
        if letter.isupper():
            return False
        if letter in string.whitespace:
            return False
        if letter in string.punctuation and letter != "_":
            return False

    return True
