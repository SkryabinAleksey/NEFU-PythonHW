def is_self_dividing(n):
    string_repr = str(abs(n))
    get_digit_dividing = 0
    for digit in string_repr:
        if (n % int(digit)) > 0:
            get_digit_dividing +=1
    if get_digit_dividing == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_self_dividing(128))
    print(is_self_dividing(635))
    print(is_self_dividing(36))