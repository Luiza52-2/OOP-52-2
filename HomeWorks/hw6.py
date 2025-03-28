def two_sum(nums, target):
    num_to_index = {}

    for index, number in enumerate(nums):
        complement = target - number

        if complement in num_to_index:
            return [num_to_index[complement], index]

        num_to_index[number] = index

    return None


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Вывод: [0, 1]