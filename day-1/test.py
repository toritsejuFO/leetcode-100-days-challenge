from solution import Solution

# An array of tuples representing the input params and return value in order
sample_test_cases = [
    ([2,7,11,15], 9, [0, 1]),
    ([3,2,4], 6, [1, 2]),
    ([3,3], 6, [0, 1])
]

if __name__ == '__main__':
    under_test = Solution()
    for test_case in sample_test_cases:
        retval = under_test.twoSum(test_case[0], test_case[1])
        assert retval == test_case[2]
    print('Completed successfully')
