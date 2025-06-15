import re
def normalize_phone(phone_number):
    # Remove all exept numbers and liave + at the begining of string
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # Chek for '+380' at the beginig
    if cleaned.startswith("+380"):
        return cleaned

    # If begining with '380', add '+'
    if cleaned.startswith("380"):
        return '+' + cleaned

    # Other conditions: chek if it starts with + but no internationtal code
    cleaned = re.sub(r"^\+", "", cleaned)
    return '+38' + cleaned

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ","33333333"
]
filtered_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", filtered_numbers)
