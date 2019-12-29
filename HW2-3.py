def count_unique_codes(words):
    morse_base = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    alphabet = [chr(l) for l in range(ord("a"), ord("z")+1)]
    dict = {}
    for k, v in zip(alphabet, morse_base):
        dict[k] = v
    words2 = set()
    for w in words:
        str = ""
        for j in range(len(w)):
            str = str + dict[w[j]]
        words2.add(str)
    return len(words2)


if __name__ == '__main__':
    words = input("words = ").split()
    print(count_unique_codes(words))