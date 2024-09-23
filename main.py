class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        
        # Start with the current level's first node
        current = root
        
        while current:
            # Use a dummy node to manage connections at the next level
            dummy = Node(0)
            tail = dummy
            
            # Iterate through the current level
            node = current
            while node:
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                
                node = node.next  # Move to the next node in the current level
            
            # Move to the next level
            current = dummy.next
        
        return root

# Example usage:
# Constructing the binary tree: [1,2,3,4,5,null,7]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

solution = Solution()
solution.connect(root)

# Output the next pointers
def print_next_pointers(node):
    while node:
        print(node.val, "->", node.next.val if node.next else "None", end=' ')
        node = node.next

print_next_pointers(root)        # Level 1
print_next_pointers(root.left)   # Level 2
print_next_pointers(root.left.left)  # Level 3

