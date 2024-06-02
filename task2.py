def coincidence(inputList: list | None = None, inputRange: range | None = None) -> list | None:
    if inputList is None or inputRange is None:
        return []
    result = [
        x
        for x in inputList
        if (
            isinstance(x, (float, int)) and (x >= inputRange[0] and x <= inputRange[-1])
        )
    ]
    return result


if __name__ == "__main__":
    print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
    print(coincidence())
    print(coincidence([None, 1, "foo", 4, 2, 2.5], range(1, 4)))
