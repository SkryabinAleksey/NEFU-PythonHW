def get_sorted_squares(nums):
    return sorted([int(n)**2 for n in nums])


if __name__ == '__main__':
    numbers = input('Spisok chisel: ').split()
    print(get_sorted_squares(numbers))