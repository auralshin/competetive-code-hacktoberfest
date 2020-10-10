'''
Binary Search Tree (BST)
new data < node goto left child
new data > node goto right child

### INPUT ###
7
3
5
2
1
4
6
7
### OUTPUT ###
Height of tree is 3

     3
   2   5
  1   4 6
         7

BFS is 3 2 5 1 4 6 7
DFS is 3 2 1 5 4 6 7
'''

# create a node, assign children to None
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    # insert new data
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    # get the height of the BST
    maxHeight = 0
    height = 0
    def getHeight(self,root):
        if root.left:
            self.height += 1
            if self.height > self.maxHeight:
                self.maxHeight = self.height
            self.getHeight(root.left)
            self.height -= 1
        if root.right:
            self.height += 1
            if self.height > self.maxHeight:
                self.maxHeight = self.height
            self.getHeight(root.right)
            self.height -= 1
        return self.maxHeight

    # Breadth First Search (aka level order)
    # output print space seperated 'explored' values
    def bfs(self, root):
        queue = []
        bfs_search = []
        # append root
        if root != None:
            queue.append(root)

            # while there are nodes to process
            while len(queue) > 0:
                # dequeue the list (FIFO)
                n = queue.pop(0)

                # process tree data
                bfs_search.append(n.data)

                # enqueue child elements from next level in order (L->R)
                if n.left != None:
                    queue.append(n.left)
                if n.right != None:
                    queue.append(n.right)

        print(f'bfs result: {bfs_search}')

    # Depth First Search (aka pre-order)
    dfs_search = []
    def dfs(self, root):
        if root != None:
            # process tree data
            self.dfs_search.append(root.data)

            # process child elements
            self.dfs(root.left)
            self.dfs(root.right)




T=int(input())
myTree=Solution()
root=None
# populate the BST
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data) # root of bst is returned (eg. node which containts self.data = 3)
# get height of the BST
height=myTree.getHeight(root)
print(f'Height = {height}')
myTree.bfs(root)
myTree.dfs(root)
print(f'dfs result {myTree.dfs_search}')