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

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ct = 0
        while ct < 500:
            val = 0
            arr = [int(i) for i in str(n)]
            for i in arr:
                val += i * i
            if val == 1:
                return True
            else:
                n = val
                ct += 1
        return False

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        while temp:
            while temp.next and temp.next.val == temp.val:
                temp.next = temp.next.next
            temp = temp.next
        return head

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        bounds: 1 <= n <= 45
        0 = 0
        1 = 1; 1
        2 = 1 1; 2; 2
        3 = 1 1 1; 1 2; 2 1; 3
        4 = 1 1 1 1; 1 1 2; 1 2 1; 2 1 1; 2 2; 5
        5 = 1 1 1 1; 1 1 1 2; 1 1 2 1; 1 2 1 1; 2 1 1 1; 1 2 2; 2 1 2; 2 2 1; 8
        """
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        m = str(bin(n))
        for i in m:
            if i == '1':
                count += 1
        return count

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]

        return nums1


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Use in main for testing
    # h = ListNode(1, ListNode(1, ListNode(2)))


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    res = sol.merge(nums1, m, nums2, n)
    print(res)
    pass
