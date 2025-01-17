class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            last = m+n-1
            #Merge in Reverse order
            while m > 0 and n > 0:
                if nums1[m-1] > nums2[n-1]:
                        nums1[last] = nums1[m-1]
                        m -= 1
                else:
                      nums1[last] = nums2[n-1]
                      n -= 1
                last -= 1
            #fill in the leftover elements in second array
                while n > 0:
                      nums1[last] = nums2[n-1]
                      last, n = last-1, n-1 

            #Time Complexity: O(m + n) Space Complexity: O(1)