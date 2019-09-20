def get_largest_perimiter(L):
    p = 0
    for i in range(len(L)-2):
        for j in range(i+1, len(L)-1):
            for k in range(j+1, len(L)):
                a = float(L[i])
                b = float(L[j])
                c = float(L[k])
                if b + c > a and a + c > b and a + b > c and a + b + c > p:
                    p = a + b + c
    if p == 0:
        return False
    else:
        return print(p)


if __name__ == "__main__":
    str = input('Spisok L: ')
    L = str.split()
get_largest_perimiter(L)
