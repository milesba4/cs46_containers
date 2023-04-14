'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''
import copy
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
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
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
        node_copy = copy.copy(node)
        # temp for new roo
        if node_copy.right:
            new_root = Node(node.right.value)
            new_root.left = Node(node.value)
            new_root.right = node_copy.right.right
            new_root.left.left = node_copy.left
            new_root.left.right = node_copy.right.left
        return new_root

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
        node_copy = copy.copy(node)
        if node_copy.left:
            new_root = Node(node.left.value)
            new_root.right = Node(node.value)
            new_root.left = node_copy.left.left
            new_root.right.right = node_copy.right
            new_root.right.left = node_copy.left.right
        return new_root

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
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        # BST insert
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        return node

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''

        if AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 1:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < -1:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree.right_rotate(node)
