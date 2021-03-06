# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if q.val < p.val: p, q = q, p

        while root:
            if q.val < root.val: root = root.left
            elif root.val < p.val: root = root.right
            else: return root
            
            
            
'''
        def findDes(root, x): 
            path = []
            while True:
                if x.val == root.val:
                    path.append(root)
                    return path
                elif x.val < root.val:
                    path.append(root)
                    root = root.left
                else: 
                    path.append(root)
                    root = root.right
        
        ppath = findDes(root, p)
        qpath = findDes(root, q)
        
        while root:
            if root.val == p.val: return root
            elif 
                
            
            
        
                5
            3       6
          2   4   n   n
        1
 '''                    