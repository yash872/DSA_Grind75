# Combination Sum
# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i, target):
            # Base Case
            if i == len(candidates):
                if target == 0:
                    res.append(curr.copy())
                    # appending copy, as curr will modify later
                return
            
            # Pick
            if candidates[i]<=target:
                curr.append(candidates[i])
                dfs(i, target-candidates[i])
                curr.pop()
            
            # Not Pick
            dfs(i+1, target)
        
        # Call
        dfs(0,target)
        return res