def popular_words(text: str, words: list[str]):
    list_of_words = text.split(" ")
    new_list = [word.lower() for word in list_of_words]
    res = {}
    for word in words:
        if word in new_list:
            res[word] = new_list.count(word)
        else:
            res[word] = 0
    return res


my_string = "When I was One I had just begun When I was Two I was nearly new"
words_list = ["i", "was", "three", "near"]
print(popular_words(my_string, words_list))
assert popular_words(my_string, words_list) == {
    "i": 4,
    "was": 3,
    "three": 0,
    "near": 0,
}, "Test1"
print("OK")
