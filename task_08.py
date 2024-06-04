def multiply_numbers(inputs=None) -> None | int:
    # Приводим вход к строке
    str_input = str(inputs)
    mult = 1
    hasDigits = False;
    # В цикле, если символ -- цифра, домножаем на него, иначе пропускаем
    for char in str_input:
        try:
            digit = int(char)
            mult *= digit
            hasDigits = True
        except ValueError:
            continue
    if not hasDigits:
        return None
    else:
        return mult

if __name__ == "__main__":
    print(multiply_numbers())
    print(multiply_numbers('ss'))
    print(multiply_numbers('1234'))
    print(multiply_numbers('sssdd34'))
    print(multiply_numbers(2.3))
    print(multiply_numbers([5,6,4]))
