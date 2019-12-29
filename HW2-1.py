def number_of_matches(J, S):
    k = 0
    j = set(J)
    s = list(S)
    for i in j:
        if i in s:
            k = k + s.count(i)
    return k


if __name__ == '__main__':
    J = input("J = ")
    S = input("S = ")
    print(number_of_matches(J, S))