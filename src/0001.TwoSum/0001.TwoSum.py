class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # used to store the value and the index of its complamentary
        dic = {}
        for i in range(len(nums)):
            # if current value is not in the dictionary, then add it
            if nums[i] not in dic:
                dic[target - nums[i]] = i
            # if current value is found in the dictionary, it is saying that its complemenary appeared before
            else:
                return [i, dic[nums[i]]]