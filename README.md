# Shortest Path in Binary Matrix

LeetCode 1091 – Shortest Path in Binary Matrix (8-directional BFS)

## 📌 Problem

Given an n × n binary matrix `grid`, return the length of the shortest clear path from the top-left cell `(0,0)` to the bottom-right cell `(n-1,n-1)`.  
A path may move in any of the 8 directions and can only visit cells with value `0`.

If no path exists, return `-1`.

## 🚀 Solution

- **Algorithm**: Breadth-First Search (BFS)
- **Time Complexity**: O(n²)
- **Space Complexity**: O(n²)
- **Key Idea**: Expand ring by ring from the start cell. The first time we reach the target, it is guaranteed to be the shortest path.

## 🧪 Examples

```python
sol = Solution()
print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))           # 2
print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))  # 4
print(sol.shortestPathBinaryMatrix([[1,0],[0,0]]))           # -1
print(sol.shortestPathBinaryMatrix([[0]]))                   # 1
