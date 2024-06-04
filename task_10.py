import re

def count_words(string:str) -> dict[str,int]:
    stat = {}
    lowercase_nopunct = re.sub(r'[^a-z]',' ',string.lower())

    words_list = lowercase_nopunct.split(sep=" ")
    for word in words_list:
        stat[word] = stat.get(word,0) + 1

    if(stat.get("",0) != 0):
        stat.pop("")

    return stat

if __name__ == "__main__":
    print(count_words("A man, a plan, a canal -- Panama"))
    print(count_words("Doo bee doo bee doo"))
