from typing import List, Optional
from collections import deque

# 144. Binary Tree Preorder Traversal\
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
#         result = []
#         if root is None:
#             return result

#         stack = [root]
#         while stack:
#             node = stack.pop()
#             result.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return result
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)

                stack.append(node.right)
                stack.append(node.left)
        return result

root_values = [1,2,3,4,5,None,8,None,None,6,7,9]
root = build_tree(root_values)

root_list = [1,2,3,4,5,None,8,None,None,6,7,9]
root = build_tree(root_list)
print(preorderTraversal(root))