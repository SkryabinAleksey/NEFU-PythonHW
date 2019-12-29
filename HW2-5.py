def is_valid(braces_string):
    k = 0
    for i in range(len(braces_string)):
        if braces_string[i] == "(":
            k = k + 1
        if braces_string[i] == ")":
            k = k - 1
        if k < 0:
            return False
            break
    if k == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    braces_string = input("braces_string = ")
    print(is_valid(braces_string))