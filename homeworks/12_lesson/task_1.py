import re


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with open(html_file, "r", encoding="utf-8") as file:
        html = file.read()

    reg_exp_pattern = r"<[^>]+>"
    resalt = re.sub(reg_exp_pattern, "", html)
    non_empty_lines = [line for line in resalt.splitlines() if line.strip()]
    cleaned_text = "\n".join(non_empty_lines)

    with open(result_file, mode="w", encoding="utf-8") as file:
        file.write(cleaned_text)


delete_html_tags("draft.html")
