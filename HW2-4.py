def get_most_frequent(words, k):
    setwords = set(words)
    list = []
    for w in setwords:
        if w in words:
            list.append([w, words.count(w)])
    list.sort(key=lambda x: x[1], reverse=True)
    return [list[i][0] for i in range(k)]


if __name__ == '__main__':
    words = input("words = ").split()
    k = int(input("k = "))
    print(get_most_frequent(words, k))