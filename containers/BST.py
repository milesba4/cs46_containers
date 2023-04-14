'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree file.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    That means that the BST class "inherits" all of the methods from BinaryTree,
    and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()

        if xs:
            self.insert_list(xs)

    def __iter__(self):
        if self.root is None:
            # returning iter type
            return iter([])
        return self._iter_(self.root)

    @staticmethod
    def _iter_(node):
        """
        Recursively yield the values in the BST in sorted order.
        """
        if node.left:
            yield from (BST._iter_(node.left))
        yield node.value
        if node.right:
            yield from (BST._iter_(node.right))

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:
        it only checks if the children of the current node are less than/greater than,
        rather than ensuring that all nodes to the left/right are less than/greater than.

        HINT:
        Use the _find_smallest and _find_largest functions to fix the bug.
        You should use the _ prefixed methods because those are static methods just like this one.
        '''
        ret = True
        if node.left:
            # curr node val must be greater than the largst value in the left
            # subtree
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            # curr node val must be smaller than the smallest value in the
            # right subtree
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.

        FIXME:
        Implement this function.

        HINT:
        Create a staticmethod helper function following the pattern of _is_bst_satisfied.
        '''
        if self.root:
            return BST._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        if node.value >= value:
            if node.left:
                return BST._insert(node.left, value)
            else:
                node.left = Node(value)
        if node.value < value:
            if node.right:
                return BST._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.

        HINT:
        Repeatedly call the insert method.
        You cannot get this method to work correctly until you have gotten insert to work correctly.
        '''

        for x in xs:
            if self.root:
                BST._insert(self.root, x)
            else:
                self.root = Node(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
        if self.root is None:
            return None
        return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        start = node
        if start.value == value:
            return True

        if start.value > value:
            if start.left:
                return BST._find(value, start.left)
            else:
                return False

        if start.value < value:
            if start.right:
                return BST._find(value, start.right)
            else:
                return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            return None
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        This is a helper function for find_smallest and not intended to be called directly by the user.
        '''
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME
        Implement this function.

        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if self.root is None:
            return None
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        '''
        helper function
        '''
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        You should have everything else working before you implement this function.

        HINT:
        Use a recursive helper function.
        '''
        if self.root:
            if self.find(value):
                self.root = BST._remove(self.root, value)
                return self.root
            return self.root
        return self.root

    @staticmethod
    def _remove(node, value):
        if node is None:
            return node
        # if node's value is greater than value move left
        if value < node.value:
            node.left = BST._remove(node.left, value)
            return node
        # if node's value is less than value move left
        elif value > node.value:
            node.right = BST._remove(node.right, value)
            return node
        # found target node
        if node.value == value:
            if node.left is None and node.right is None:
                node = None
                return node
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                succ_parent = node
                succ = node.right
                while succ.left is not None:
                    succ_parent = succ
                    succ = succ.left
                if succ_parent != node:
                    succ_parent.left = succ.right
                else:
                    succ_parent.right = succ.right
                node.value = succ.value
                return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.

        HINT:
        See the insert_list function.
        '''
        for x in xs:
            BST.remove(self, x)


bst = BST()
bst.root = Node(0)
bst.root.left = Node(-2)
bst.root.left.left = Node(-3)
bst.root.left.right = Node(1)
bst.root.right = Node(2)
bst.root.right.left = Node(1)
bst.root.right.right = Node(3)