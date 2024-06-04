def filter_dict(dictionary: dict, less_than: int) -> dict:
    """Удалить из словаря элементы, чей ключ меньше 10"""
    return {k: v for k, v in dictionary.items() if v >= less_than}


def connect_dicts(dict1: dict, dict2: dict) -> dict:
    res = {}
    dict1_sum = sum(dict1.values())
    dict2_sum = sum(dict2.values())
    if dict1_sum <= dict2_sum:
        res = filter_dict(dict1, 10) | filter_dict(dict2, 10)
    else:
        res = filter_dict(dict2, 10) | filter_dict(dict1, 10)

    # Отсортировать полученный словарь по значениям
    res = dict(sorted(res.items(), key=lambda x: x[1]))

    return res


if __name__ == "__main__":
    print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
    print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
    print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
