from solution import Solution

# An array of tuples representing the expected input params and return value in order
sample_test_cases = [
    ('()', True),
    ('()[]\{\}', False),
    ('(]', False)
]

if __name__ == '__main__':
    under_test = Solution()
    for test_case in sample_test_cases:
        retval = under_test.isValid(test_case[0])
        assert retval == test_case[1]
    print('Completed successfully')
