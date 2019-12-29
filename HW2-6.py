def get_two_sum(nums, k):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if int(nums[i]) + int(nums[j]) == k:
                return [i, j]


if __name__ == '__main__':
    nums = input("nums = ").split()
    k = int(input("target = "))
    print(get_two_sum(nums, k))