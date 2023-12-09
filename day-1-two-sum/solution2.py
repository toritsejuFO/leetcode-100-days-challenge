# Hash map solution - O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retval = None
        hm = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm:
                return [hm.get(diff), i]
            hm[nums[i]] = i

        return retval
