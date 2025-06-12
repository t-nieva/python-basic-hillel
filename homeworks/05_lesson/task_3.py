import string

prohibited_characters = string.punctuation + " "


def create_hashtag(my_str: str) -> str:
    words_list = my_str.split()
    capitalized_list = [word.capitalize() for word in words_list]
    capitalized_str = "".join(capitalized_list)
    cleaned_str = "".join(
        char for char in capitalized_str if char not in prohibited_characters
    )
    hashtag = "#" + cleaned_str
    return hashtag[:140]
