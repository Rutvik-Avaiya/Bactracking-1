
class Solution:
  def combinationSum(self, candidates, target):
    ans = []

    def dfs(s: int, target: int, path) -> None:
      if target < 0:
        return
      if target == 0:
        ans.append(path.clone())
        return

      for i in range(s, len(candidates)):
        path.append(candidates[i])
        dfs(i, target - candidates[i], path)
        path.pop()

    candidates.sort()
    dfs(0, target, [])
    return ans