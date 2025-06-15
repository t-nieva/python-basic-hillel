def get_day_word(n: int) -> str:
    last_two = n % 100
    last = n % 10

    if 11 <= last_two <= 14:
        return "днів"
    elif last == 1:
        return "день"
    elif 2 <= last <= 4:
        return "дні"
    else:
        return "днів"


total_seconds = int(
    input(
        "Please enter a number greater than or equal to 0 " "and less than 8,640,000: "
    )
)

days, remainder = divmod(total_seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

result = f"{days} {get_day_word(days)}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(result)
