class Solution:
    def sortArray(self, nums):
        
        def quicksort(left, right):
            if left >= right:
                return
            
            pivot = nums[right]  # choose last element as pivot
            i = left
            
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            # place pivot in correct position
            nums[i], nums[right] = nums[right], nums[i]
            
            # recursively sort left & right
            quicksort(left, i - 1)
            quicksort(i + 1, right)
        
        quicksort(0, len(nums) - 1)
        return nums
