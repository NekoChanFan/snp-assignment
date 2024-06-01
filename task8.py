def multiply_numbers(inputs=None) -> None | int:
    str_input = str(inputs)
    mult = 1
    hasDigits = False;
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

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5,6,4]))
