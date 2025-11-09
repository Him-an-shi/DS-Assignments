'''17	Implement various operations on a Binary Search Tree, 
such as insertion, deletion, display (inorder, preporder and postorder traversal) and search.'''

class TreeNode(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:  
    def insert(self,root,value):
        if root is None:
            return TreeNode(value)
        curr=root
        while curr:
            if curr.data>value:
                if curr.left:
                    curr=curr.left
                else:
                    curr.left=TreeNode(value)
                    break
            elif curr.data<value:
                if curr.right:
                    curr=curr.right
                else:
                    curr.right=TreeNode(value)
                    break
            else:
                print("Already in the Tree")
        return root
    
    def search(self,root,value):
        if  root is None:
            return None
        curr=root
        while curr:
            if curr.data==value:
                return curr
            elif curr.data<value:
                curr=curr.right
            else:
                curr=curr.left             
        return None
    
    def delete(self,root,value):
        curr=root
        if value<curr.data:
            curr.left=self.delete(curr.left,value)
        elif value>curr.data:
            curr.right=self.delete(curr.right,value)
        else:
            if not curr.left and not curr.right:
                return None
            if not curr.left:
                return curr.right
            if not  curr.right:
                return curr.left
            succ=self.get_successor(curr.right)
            curr.data=succ.data
            curr.right=self.delete(curr.right,succ.data)
        return root
     
    def get_successor(self,node):
        while node.left:
            node=node.left
        return  node
    
    def display_inorder(self,root):
        stack=[]
        result=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.data)
            curr=curr.right
        return result
    
    def display_preorder(self,root):
        if not root:
            return []
        stack=[root]
        result=[]
        while stack:
            curr=stack.pop()
            result.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result
    
    def display_postorder(self,root):
        if not root:
            return []
        stack=[root]
        result=[]
        while stack:
            curr=stack.pop()
            result.append(curr.data)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result[::-1]
    
bst = BST()
root = None

while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert a node")
    print("2. Search for a node")
    print("3. Delete a node")
    print("4. Display Inorder Traversal")
    print("5. Display Preorder Traversal")
    print("6. Display Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        root = bst.insert(root, val)
        print(f"{val} inserted.")

    elif choice == 2:
        val = int(input("Enter value to search: "))
        result = bst.search(root, val)
        print(f"{val} found." if result else f"{val} not found.")

    elif choice == 3:
        val = int(input("Enter value to delete: "))
        root = bst.delete(root, val)
        print(f"{val} deleted (if it existed).")

    elif choice == 4:
        print("Inorder Traversal:", bst.display_inorder(root))

    elif choice == 5:
        print("Preorder Traversal:", bst.display_preorder(root))

    elif choice == 6:
        print("Postorder Traversal:", bst.display_postorder(root))

    elif choice == 7:
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
