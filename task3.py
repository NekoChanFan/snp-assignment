def max_odd(array):
    max_odd = 0
    try:
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
    except TypeError:
        return None


def f(x):
    x[2] = 10


if __name__ == "__main__":
    print(max_odd([2, "ololo", 1, 32, None, 4, [1]]))
    print(max_odd(10))
