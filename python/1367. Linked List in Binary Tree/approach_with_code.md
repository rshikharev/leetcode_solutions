[Binary Tree Path Matching Using DFS 🌳🔗 - LeetCode Post](https://leetcode.com/problems/linked-list-in-binary-tree/solutions/5750492/binary-tree-path-matching-using-dfs/)

# Intuition
My first thought was to use Depth-First Search (DFS) to explore possible paths in the binary tree and check if they match the sequence of nodes in the linked list. Each node in the binary tree can potentially be the starting point of a downward path, so the solution needs to explore the tree nodes and compare them with the linked list.

# Approach
1. I defined a helper function `dfs` that checks whether the current path in the binary tree matches the linked list. The function takes a binary tree node and a linked list node and recursively checks if their values match.
2. If a match is found, the function recursively explores both the left and right subtrees, trying to continue matching the linked list.
3. To handle cases where the linked list might start at any node in the binary tree, I used another helper function `traverse`, which explores every node in the binary tree. It checks whether the `dfs` function can find a matching path starting at the current tree node.
4. Finally, I call the `traverse` function starting from the root of the binary tree.

### How the algorithm solves examples:

1. **Example 1**: 
    - Input: `head = [4,2,8]`, `root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
    - The DFS starts from node `4` in the binary tree, where it finds a match with the head of the linked list. It continues down the left subtree, matching nodes `2` and `8`. The function returns `True` since it finds the whole linked list as a downward path.
    
2. **Example 2**: 
    - Input: `head = [1,4,2,6]`, `root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
    - The DFS finds a match starting from the root node `1`. The path continues down, matching nodes `4`, `2`, and `6`. Thus, the function returns `True`.
    
3. **Example 3**: 
    - Input: `head = [1,4,2,6,8]`, `root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
    - Although the path `1 -> 4 -> 2 -> 6` exists, the linked list has an additional node `8`. Since this node does not match any node downward in the binary tree, the function returns `False`.

# Complexity
- Time complexity: The time complexity is $$O(T \times L)$$, where $$T$$ is the number of nodes in the binary tree and $$L$$ is the length of the linked list. This is because for each node in the tree, we might need to compare the entire linked list.
  
- Space complexity: The space complexity is $$O(H)$$, where $$H$$ is the height of the binary tree due to the recursion stack used during the DFS.

I welcome any suggestions or advice on optimizing this code!


# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Function to check if a path starting from a tree node matches the linked list
        def dfs(tree_node: TreeNode, list_node: ListNode) -> bool:
            if not list_node:  # If we have fully traversed the linked list
                return True  # All nodes of the linked list are matched
            if not tree_node:  # If the tree node is null before matching the list completely
                return False  # The path doesn't exist
            
            # Check if the current tree node matches the current list node
            if tree_node.val == list_node.val:
                # Recursively check for both left and right subtrees
                return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
            
            return False  # No match found

        # Function to traverse the binary tree
        def traverse(tree_node: TreeNode) -> bool:
            if not tree_node:  # If the current tree node is null
                return False
            
            # Check if the current tree node can start a matching path
            if dfs(tree_node, head):
                return True
            
            # Otherwise, traverse the left and right subtree
            return traverse(tree_node.left) or traverse(tree_node.right)

        # Start the tree traversal from the root
        return traverse(root)
```
