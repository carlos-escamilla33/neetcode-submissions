class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix) - 1

        while L <= R:
            outerMid = (L + R) // 2
            l = 0
            r = len(matrix[outerMid]) - 1
            while l <= r:
                innerMid = (l + r) // 2
                if matrix[outerMid][innerMid] == target:
                    return True
                elif matrix[outerMid][innerMid] > target:
                    r = innerMid - 1
                else:
                    l = innerMid + 1
            if matrix[outerMid][0] > target:
                R = outerMid - 1
            else:
                L = outerMid + 1
    
        return False





"""
Goal find the target in the matrix

binary search approach
lets us know from the start being it reiterates that the #'s are in order

l = 0
r = len(matrix) - 1

while l <= r:
    outerMid = (l + r) // 2
    L = 0
    R = len(matrix[outerMid])

    while L <= R:
        innerMid = (L + R) // 2

        if matrix[outerMid][innerMid] == target:
            return True
        elif matrix[outerMid][innerMid] > target:
            R = innerMid - 1
        else:
            L = innerMid + 1
    
    if the value the first index of the array of the current index is greater than the target
        r = mid - 1
    else:
        l = mid + 1

return false if not found
"""