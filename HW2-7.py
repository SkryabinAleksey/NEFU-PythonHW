def get_three_sum(nums, k):
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for l in range(j + 1, len(nums)):
                if int(nums[i]) + int(nums[j]) + int(nums[l]) == k:
                    return [i, j, l]


if __name__ == '__main__':
    nums = input("nums = ").split()
    k = int(input("target = "))
    print(get_three_sum(nums, k))