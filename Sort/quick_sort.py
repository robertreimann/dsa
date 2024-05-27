class QuickSort:
    def sort(nums):
        def quick_sort(l, r):
            if r <= l:
                return
            
            partition = QuickSort.partition(nums, l, r)
            quick_sort(l, partition)
            quick_sort(partition + 1, r)

        quick_sort(0, len(nums) - 1)
        return nums
    
    # (almost) quickselect / Hoare's selection algorithm but without the recursion
    # 1. Select the first element (l) as the pivot.
    # 2. Initialize two pointers as l - 1 and r + 1 (offset because we increment/decrement in the loop)
    # 3. Move the two pointers closer to each other by 1
    # 4. Move the left pointer along as long as the number it points to is lesser than pivot
    # 5. Move the right pointer along as long as the number it points to is greater than pivot.
    # 6. If the pointers met, then it must be correct that to the left of the pivot there are only elements smaller than it
    # and to the right there are only elements greater than it, so return the pivot (the right pointer).
    # 7. If they didn't meet then the left pointer found a value greater than pivot and right pointer found an element that is less than the pivot.
    # so swap the elements and try again.
    def partition(nums, l, r):
        i, j = l - 1, r + 1
        while True:
            i += 1
            j -= 1
            while nums[i] < nums[l]: i += 1
            while nums[j] > nums[l]: j -= 1

            if i >= j: return j
            nums[i], nums[j] = nums[j], nums[i]
    
array = [30, 36, 16, 11, 22, 48, 32, 18, 3, 29, 2, 24, 33, 33, 15, 3, 0, 44, 8, 11, 31, 26, 49, 0, 28, 40, 22, 44, 28, 6, 47, 47, 28]
# [30, 36, 16, 11, 22, 48, 32, 18, 3, 29, 2, 24, 33, 33, 15, 3, 0, 44, 8, 11, 31, 26, 49, 0, 28, 40, 22, 44, 28, 6, 47, 47, 28]
print(array)
# [0, 0, 2, 3, 3, 6, 8, 11, 11, 15, 16, 18, 22, 22, 24, 26, 28, 28, 28, 29, 30, 31, 32, 33, 33, 36, 40, 44, 44, 47, 47, 48, 49]
print(QuickSort.sort(array))
