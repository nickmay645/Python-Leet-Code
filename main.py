# Leet Code Practice

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in values:
                return [i, values[remaining]]
            else:
                values[num] = i


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    sol = Solution
    res = sol.twoSum(sol, nums, target)
    pass
