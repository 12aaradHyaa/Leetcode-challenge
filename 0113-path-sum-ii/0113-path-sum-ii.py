
class Solution:
    def pathSum(self, root, targetSum):
        result = []
        path = []

        def dfs(node, remaining):
            if node is None:
                return

            path.append(node.val)
            remaining -= node.val

            # Check if this is a leaf node
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path.copy())
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)

            # Backtracking
            path.pop()

        dfs(root, targetSum)
        return result
