class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retval = None
        num_len = len(nums)

        for i in range(num_len):
            j = i + 1
            while j < num_len:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j = j + 1

        return retval
