def remove_tags(text):
    result = ""
    inside_tag = False

    for char in text:
        if char == "<":
            inside_tag = True
        elif char == ">":
            inside_tag = False
            continue
        if not inside_tag and char != ">":
            result += char
    return result


def remove_space(text):
    non_empty_lines = [line for line in text.splitlines() if line.strip()]
    cleaned_text = "\n".join(non_empty_lines)
    return cleaned_text


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with open(html_file, "r", encoding="utf-8") as file:
        html = file.read()
        cleaned_text = remove_tags(html)
        cleaned_text = remove_space(cleaned_text)
        print(cleaned_text)

    with open(result_file, mode="w", encoding="utf-8") as file:
        file.write(cleaned_text)


delete_html_tags("draft.html")
