from solution import Solution

# An array of tuples representing the expected input params and return value in order
sample_test_cases = [
    ('abc', 'pqr', 'apbqcr'),
    ('ab', 'pqrs', 'apbqrs'),
    ('abcd', 'pq', 'apbqcd')
]

if __name__ == '__main__':
    under_test = Solution()
    i = 1
    for test_case in sample_test_cases:
        retval = under_test.mergeAlternately(test_case[0], test_case[1])
        assert retval == test_case[2]
        print (f'TestCase_{i}: {retval == test_case[2]}')
        i += 1
    print('Completed successfully')
