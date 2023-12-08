from solution1 import Solution as Solution1
from solution2 import Solution as Solution2

# An array of tuples representing the input params and return value in order
sample_test_cases = [
    (121, True),
    (-121, False),
    (10, False),
    (1000000001, True),
    (1000030001, False)
]

if __name__ == '__main__':
    under_test1 = Solution1()
    for test_case in sample_test_cases:
        retval = under_test1.isPalindrome(test_case[0])
        assert retval == test_case[1]
    print('Solution 1 Completed successfully')

    under_test2 = Solution2()
    for test_case in sample_test_cases:
        retval = under_test2.isPalindrome(test_case[0])
        assert retval == test_case[1]
    print('Solution 2 Completed successfully')
