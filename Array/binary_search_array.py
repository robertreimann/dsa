class BinarySearch:
    # O(logn) (assumes array is sorted)
    
    # Did you forget something checklist:
    # 1. Did you set the left/right pointer to mid +1/-1 instead of just mid?
    # Not sure what there is to forget here, really...

    # Standards
    # Use left, right, mid as the pointers
    # Use inclusive comparison for while loop
    # Use integer division to round down mid
    # Use (left + right) // 2 for mid point
    def binary_search_array(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
