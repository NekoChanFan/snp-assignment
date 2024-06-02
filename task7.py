def combine_anagrams(words_array: list[str]) -> list[list[str]]:
    # Словарь <отсортированное слово, массив анаграмм>
    anagram_map = {}

    for word in words_array:
        # Сортируем слово в алфавитном порядке -- ключ в маппе
        word_sorted = "".join(sorted(word))
        # Создаём новый массив, либо записываем в существующий
        anagram_map[word_sorted] = anagram_map.get(word_sorted,[]) + [word]

    return list(anagram_map.values())

if __name__ == "__main__":
    print(combine_anagrams(["cars","for", "potatoes", "racs", "four", "scar", "creams", "scream"]))

