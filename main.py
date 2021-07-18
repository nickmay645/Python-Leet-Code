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


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Use in main for testing
    # h = ListNode(1, ListNode(1, ListNode(2)))


if __name__ == '__main__':
    sol = Solution()

    res = sol.hammingWeight(0b0000000000000000000000000001011)
    print(res)
    pass
