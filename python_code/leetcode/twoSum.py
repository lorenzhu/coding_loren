class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """      

        '''
        注意: why: 返回的答案是 [0, 0] ？？？
             because: nums中可能存在重复的值，比如([3,3,4,...], 6), 所以不要用 (target-nums[i] in nums)方式查询
        
        思路： 遍历 nums 中的值，其中 item 为当前值，index 为 item 在 nums 中的索引
              查询 target-item 是否在字典中：如果不在 -->  则将 item:index 作为 key:value 存入字典
                                           如果在  --> 则返回值为 [target-item 在字典中的value, item的索引（即当前index）]
                                          (原来触发return 以后，程序就over了，不会继续运算了)
              ps: for 循环先看 else 语句比较容易理解
        '''
        search_dict = {}
        for index,item in enumerate(nums):
            if (target-item) in search_dict:
                return [search_dict[target-item], index]
            else:
                search_dict[item] = index  # 从这里开始比较好理解，
        
        '''
        # 显然用 for 循环取索引会比用 enumerate() 直接取索引要慢一些
        search_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in search_dict:
                return [search_dict[target-nums[i]], i]
            else:
                search_dict[nums[i]] = i
        '''

answer = Solution()

the2 = answer.twoSum([3,2,4], 6)
print(the2)