def max_odd(array: list) -> int | None:
    max_odd = 0
    for x in array:
        if not isinstance(x, (float, int)):
            continue
        if isinstance(x, float):
            if x.is_integer():
                x = int(x)
            else:
                continue
        if x % 2 == 1 and x > max_odd:
            max_odd = x
    if max_odd == 0:
        return None
    else:
        return max_odd


if __name__ == "__main__":
    print(max_odd([1, 2, 3, 4, 4]))
    print(max_odd([21.0, 2, 3, 4, 4]))
    print(max_odd(["ololo", 2, 3, 4, [1, 2], None]))
    print(max_odd(["ololo", "fufufu"]))
    print(max_odd([2, 2, 4]))
