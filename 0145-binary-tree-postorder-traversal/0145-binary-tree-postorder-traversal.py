class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postorder(node):
            if node is None:
                return

            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

        postorder(root)
        return result
