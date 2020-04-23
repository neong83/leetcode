# Third attemp:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # replace merged sort with python build-in sorted method to speed up process time
	merged_nums = sorted(nums1 + nums2)
        
        length_of_merged_nums = len(merged_nums)
        median_position, has_one_median = length_of_merged_nums // 2, length_of_merged_nums % 2
        
        median_num = merged_nums[median_position]
        
        if not has_one_median:
            return (merged_nums[median_position - 1] + median_num) / 2
        
        return median_num


# Second attemp:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                merged_nums.append(nums1.pop(0))
            else:
                merged_nums.append(nums2.pop(0))
        
        while nums1:
            merged_nums.append(nums1.pop(0))
            
        while nums2:
            merged_nums.append(nums2.pop(0))
        
	# replace `divmod` with (x//2, x %2) speed up the execution times
        length_of_merged_nums = len(merged_nums)
        median_position, has_one_median = length_of_merged_nums // 2, length_of_merged_nums % 2
        
        median_num = merged_nums[median_position]
        
        if not has_one_median:
            return (merged_nums[median_position - 1] + median_num) / 2
        
        return median_num

# First attemp:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                merged_nums.append(nums1.pop(0))
            else:
                merged_nums.append(nums2.pop(0))
        
        while nums1:
            merged_nums.append(nums1.pop(0))
            
        while nums2:
            merged_nums.append(nums2.pop(0))
            
        median_position, has_one_median = divmod(len(merged_nums), 2)
        
        median_num = merged_nums[median_position]
        
        if not has_one_median:
            return (merged_nums[median_position - 1] + median_num) / 2
        
        return median_num
