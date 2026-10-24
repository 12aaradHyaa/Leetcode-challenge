class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if node is None:
                return

            result.append(node.val)  # 1. Root
            preorder(node.left)      # 2. Left
            preorder(node.right)     # 3. Right

        preorder(root)
        return result
