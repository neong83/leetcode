def twoSum(self, nums: List[int], target: int) -> List[int]:
d = dict()

for i, v in enumerate(nums):
    if v in d:
	return [d[v], i]
    
    if (result := target - v) not in d:
	d[result] = i
    
