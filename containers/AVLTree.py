'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
        if xs is not None:
            for x in xs:
                self.insert(x)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        if self.root is None:
            return True
        else:
            return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if AVLTree._balance_factor(node) not in [-1,0,1]:
            return False
        else:
            if node.left:
                ret &= AVLTree._is_avl_satisfied(node.left)
            if node.right:
                ret &= AVLTree._is_avl_satisfied(node.right)
        return ret


    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        #Create copy of node
        node_copy = node
        # Create temp var to keep track of new root of subtree (node.right)
        new_root = node_copy.right
        #replace the right child of the old root with the left child of the new.
        node_copy.right = new_root.left
        #If newRoot has a left child then the new parent of the left child becomes the old root.
        if new_root.left is not None:
            new_root.left.parent = node_copy
        #The parent of the new root is set to the parent of the old root.
        new_root.parent = node_copy.parent
        #If the old root was the root of the entire tree then we must set the root of the tree to point to this new root.
        if BST.isRoot(node_copy):
            #set self.root = new_root
            node_copy = new_root
        else:
            if node_copy.left:
                node_copy.parent.left = new_root
            else:
                node_copy.parent.right = new_root
        new_root.left = node_copy
        node_copy.parent = new_root
        return node_copy
        node_bf  =  AVLTree._balance_factor(node) + 1 - min(AVLTree._balance_factor(new_root),0)
        new_root_bf  =  AVLTree._balance_factor(new_root) + 1 + max(AVLTree._balance_factor(node),0)
    
    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
            elif AVLTree._balance_factor > 0:
                if AVLTree._balance_factor(node.left) < 0:
                    AVLTree._left_rotate(node.left)
                    AVLTree._right_rotate(node)
                else:
                    AVLTree.right_rotate(node)
        '''

avl = AVLTree()
avl.root = Node(0)
avl.root.left = Node(-2)
avl.root.left.left = Node(-3)
avl.root.left.left.left = Node(-4)
avl.root.left.right = Node(-1)
avl.root.right = Node(2)
avl.root.right.left = Node(1)
avl.root.right.right = Node(3)
avl.root.right.right.right = Node(4)
avl.root.right.right.right.right = Node(5)
