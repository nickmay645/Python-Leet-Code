# Leet Code Practice
import collections

from constraint import xrange


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

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        """

        res = set()

        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)

        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        if len(z) >= 3:
            res.add((0, 0, 0))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        nums = [-1, 2, 1, -4]
        target = 1
        The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for idx in range(len(digits)):
            result = [prev + l for prev in result for l in digit_map[digits[idx]]]
        return result

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        prev = timeSeries[0]
        poison = duration

        for i in range(1, len(timeSeries)):

            if prev + duration >= timeSeries[i]:
                overlap = prev + duration - timeSeries[i]
                poison += duration - overlap
            else:
                poison += duration

            prev = timeSeries[i]
        return poison

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        0 1 2 3 4
        n = 3
        length = 5
        0 1 3 4
        node[2]next = node[2].next.next
        """
        fast = slow = head
        for i in xrange(n):
            fast = fast.next
        if fast == None: return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l2 is None and l1 is None:
            return None

        merged = ListNode()
        merge_copy = merged
        while l2 is not None or l1 is not None:

            if l2 is None:
                merged.val = l1.val
                l1 = l1.next
            elif l1 is None:
                merged.val = l2.val
                l2 = l2.next
            elif l2.val <= l1.val:
                merged.val = l2.val
                l2 = l2.next
            else:
                merged.val = l1.val
                l1 = l1.next

            if l2 is not None or l1 is not None:
                merged.next = ListNode()
                merged = merged.next

        return merge_copy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Use in main for testing
    # h = ListNode(1, ListNode(1, ListNode(2)))


if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(1, ListNode(2))
    l2 = ListNode(1, ListNode(2))
    res = sol.mergeTwoLists(l1, l2)
    print(res)
    pass
