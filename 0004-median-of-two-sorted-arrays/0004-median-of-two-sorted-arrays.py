class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        A, B = nums1, nums2
        arrayLen = len(A) + len(B)
        middle = arrayLen // 2
        
        
        if len(A) > len(B):
            B, A = A, B
            
        l, r = 0, len(A) - 1
        
        while True:
            i = l + ((r-l) // 2)
            j = middle - i - 2
            
            aLeft = A[i] if i >= 0 else float("-infinity")
            aRight = A[i+1] if (i+1) < len(A) else float("infinity")
            bLeft = B[j] if j >= 0 else float("-infinity")
            bRight = B[j+1] if (j+1) < len(B) else float("infinity")
            
            # checks for 
            if aLeft <= bRight and bLeft <= aRight:
                # odd
                
                if arrayLen % 2:
                    print(min(bRight, aRight))
                    return min(bRight, aRight)
                # even
                else:
                    return (float(max(aLeft, bLeft) + min(aRight, bRight))) / 2 
            # if left partition A is greater
            elif aLeft > bRight:
            # increase the partition 
                r = i - 1
            else:
                l = i + 1
            

        
        
        
        
        