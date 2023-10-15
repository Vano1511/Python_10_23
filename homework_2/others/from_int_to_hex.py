BASE = "0123456789abcdef"

def to_hex(number, delimiter=16):
    result = ""
    if number < 0:
        number = abs(number)
        suffix = "-0x"
    else:
        suffix = "0x"
    while number > 0:
        index = number % delimiter
        result = BASE[index] + result
        number //= delimiter
    return suffix + result


user_input = int(input("введите целое число: "))
print(f"ответ: {to_hex(user_input)}")
print(f"проверка : {hex(user_input)}")
