def say_hi(name: str, age: int) -> str:
    """
    Return a greeting string introducing the person.

    :param name: The person`s name.
    :param age: The person age.
    :return: A greeting message.
    """
    return f"Hi. My name is {name} and I'm {age} years old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "Test1"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Test2"
print("ОК")
