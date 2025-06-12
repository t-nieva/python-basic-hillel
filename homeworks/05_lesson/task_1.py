string_punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""
kwlist = [
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]
soft_kwlist = ["case", "match", "type"]


def validate_variable(variable_name: str) -> bool:
    underscore_count = 0

    if variable_name[0].isdigit():
        return False

    if variable_name in kwlist or variable_name in soft_kwlist:
        return False

    for letter in variable_name:
        if letter.isupper():
            return False
        if letter == " ":
            return False
        if letter in string_punctuation:
            return False
        if letter == "_":
            underscore_count += 1

    if underscore_count > 1:
        return False

    return True
