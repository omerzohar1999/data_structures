# username -
# id1      -
# name1    -
# id2      -
# name2    -

import random

"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1    # changed virtual height&size so it could be maintained easily
        self.size = 0

        if value is not None:
            self.left = AVLNode(None)
            self.right = AVLNode(None)
            self.height = 0  # as a leaf
            self.size = 1

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    """returns the height

    @rtype: int
    @returns: the size of self
    """

    def getSize(self):
        return self.size

    """returns the Balance Factor
    
    @rtype: int
    @returns: the height of left - the height of right
    """

    def getBF(self):
        return self.left.getHeight() - self.right.getHeight()

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.value is None

    """returns an array containing all 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """

    def nodeToArray(self):
        left_node_array = self.getLeft().nodeToArray() if self.getLeft().isRealNode() else []
        right_node_array = self.getRight().nodeToArray() if self.getRight().isRealNode() else []
        self_array = [self.value]
        return left_node_array + self_array + right_node_array


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.size = 0
        self.root = None
        self.min_node = None
        self.max_node = None

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.size == 0

    """retrieves the node containing the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: AVLNode
    @returns: the node containing the i'th item in the list
    """

    def retrieve_node(self, i):
        pointer_node = self.min_node
        new_index = i
        while pointer_node.size < i:
            if pointer_node.size == i - 1:
                return pointer_node.parent
            elif pointer_node.parent.size > i:
                pointer_node = pointer_node.parent
            else:
                pointer_node = pointer_node.parent
        while new_index != pointer_node.getLeft().size + 1:
            if pointer_node.getLeft().size < new_index:
                new_index -= (pointer_node.getLeft().size + 1)
                pointer_node = pointer_node.getRight()
            else:
                pointer_node = pointer_node.getLeft()
        return pointer_node

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return self.retrieve_node(i).value

    """fixes the size of a node to a correct size after correction

        @type node: AVLNode
        @pre: node.left.size and node.right.size are correct
        """

    def fix_size(self, node):
        node.size = node.left.size + node.right.size + 1

    """fixes the height of a node to a correct height after correction

        @type node: AVLNode
        @pre: node.left.height and node.right.height are correct
        """

    def fix_height(self, node):
        node.height = max(node.left.height, node.right.height) + 1

    """Does an RR rotation

            @type node: AVLNode
            @pre: 0 <= search(node) < self.length()
            @param node: node in the tree
            @rtype: int
            @returns: The number of rotations - 1
            """

    def RR(self, node):
        # if node is root - takes care separately
        if node.parent is None:
            return self.LL(node.right)
        # swaps between the nodes, opposite to LL
        subtree = node.right
        decreasing_node = node.parent
        node.setRight(decreasing_node)
        decreasing_node.setLeft(subtree)
        subtree.setParent = decreasing_node
        decreasing_node.setParent(node)
        # fixes the parental connection to the swapped nodes
        node.setParent(decreasing_node.parent)
        if decreasing_node.parent is not None:
            if decreasing_node.parent.getLeft() == decreasing_node:
                decreasing_node.parent.setLeft(node)
            else:
                decreasing_node.parent.setRight(node)
        # maintain height and size
        self.fix_size(decreasing_node)
        self.fix_size(node)
        self.fix_height(decreasing_node)
        self.fix_height(node)
        return 1

    """Does a LL rotation

            @type node: AVLNode
            @pre: 0 <= search(node) < self.length()
            @param node: node in the tree
            @rtype: int
            @returns: The number of rotations - 1
            """

    def LL(self, node):
        # if node is root - takes care separately
        if node.parent is None:
            return self.RR(node.left)
        # swaps between the nodes, opposite to RR
        subtree = node.left
        decreasing_node = node.parent
        node.setLeft(decreasing_node)
        decreasing_node.setRight(subtree)
        subtree.setParent = decreasing_node
        decreasing_node.setParent(node)
        # fixes the parental connection to the swapped nodes
        node.setParent(decreasing_node.parent)
        if decreasing_node.parent is not None:
            if decreasing_node.parent.getLeft() == decreasing_node:
                decreasing_node.parent.setLeft(node)
            else:
                decreasing_node.parent.setRight(node)
        # maintain height and size
        self.fix_size(decreasing_node)
        self.fix_size(node)
        self.fix_height(decreasing_node)
        self.fix_height(node)
        return 1

    """Does an RL rotation

            @type node: AVLNode
            @pre: 0 <= search(node) < self.length()
            @param node: node in the tree
            @rtype: int
            @returns: The number of rotations - 2
            """

    def RL(self, node):
        return self.RR(node) + self.LL(node)

    """Does an LR rotation

            @type node: AVLNode
            @pre: 0 <= search(node) < self.length()
            @param node: node in the tree
            @rtype: int
            @returns: The number of rotations - 2
            """

    def LR(self, node):
        return self.LL(node) + self.RR(node)

    """Determines which rotation is needed (if needed) and does that

                @type node: AVLNode
                @pre: 0 <= search(node) < self.length()
                @param node: node in the tree
                @rtype: int
                @returns: The number of rotations, 0 if there were not any rotations
                """

    def rotate(self, node):
        if node.getBF() < -1:
            if node.right.getBF() >= 1:
                return self.RL(node.right.left)
            else:
                return self.LL(node.right)
        if node.getBF() > 1:
            if node.left.getBF() <= -1:
                return self.LR(node.left.right)
            else:
                return self.RR(node.left)
        return 0

    """Maintains AVL rules and node/tree fields.

    @type node: AVLNode
    @pre: 0 <= search(node) < self.length()
    @param node: node in the tree
    @rtype: int
    @returns: The number of rotations
    """

    def maintain(self, node):
        count_rotations = 0
        while node is not None:
            count_rotations += self.rotate(node)
            # need to fix size, height after insertion / deletion even if there is no current rotate:
            self.fix_size(node)
            self.fix_height(node)
            if node.parent is None:
                self.root = node
            node = node.parent
        self.size = self.root.size
        return count_rotations

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        def inner_insert(parent_node, son, r_l_flag):
            if r_l_flag == 'R':
                subtree = parent_node.right
                parent_node.right = son
                son.right = subtree
            if r_l_flag == 'L':
                subtree = parent_node.left
                parent_node.left = son
                son.left = subtree
            son.parent = parent_node
            if subtree.isRealNode():
                subtree.parent = son
            # fix height, size
            self.fix_size(son)
            self.fix_size(parent_node)
            self.fix_height(son)
            self.fix_height(parent_node)

        new_node = AVLNode(val)
        # take care of empty tree
        if self.size == 0:
            self.root = self.min_node = self.max_node = new_node
            return self.maintain(new_node)
        if i == 0:
            self.min_node = new_node
        if i == self.size:
            inner_insert(self.max_node, new_node, 'R')
            self.max_node = new_node
        else:
            next_node = self.retrieve_node(i + 1)
            if next_node.left.value is None:
                inner_insert(new_node, new_node, 'L')
            else:
                prev_node = self.retrieve_node(i - 1)
                inner_insert(prev_node, new_node, 'R')
        # fix AVL invariant
        return self.maintain(new_node.parent)

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        # take care of empty tree
        if self.size == 1:
            self.root = self.min_node = self.max_node = AVLNode(None)
            self.size = 0
            return 0
        # maintain min_node, max_node
        if i == 0:
            self.min_node = self.retrieve_node(1)
        if i == self.size - 1:
            self.max_node = self.retrieve_node(self.size - 2)
        # perform a regular deletion
        deleted_node = self.retrieve_node(i)

        def inner_delete(node):
            if node.left.value is not None and node.right.value is not None:
                successor = self.retrieve_node(i + 1)
                node.value = successor.value
                node = successor
                inner_delete(node)
            else:
                if node.left.value is None:  # has only right son or no sons at all
                    node.right.parent = node.parent
                    if node.parent is not None:
                        if node.parent.left == node:
                            node.parent.left = node.right
                        else:
                            node.parent.right = node.right
                        self.fix_size(node.parent)
                        self.fix_height(node.parent)
                else:   # has only left son
                    node.left.parent = node.parent
                    if node.parent is not None:
                        if node.parent.left == node:
                            node.parent.left = node.left
                        else:
                            node.parent.right = node.left
                        self.fix_size(node.parent)
                        self.fix_height(node.parent)
            return node

        deleted_node = inner_delete(deleted_node)
        # fix AVL invariant
        return self.maintain(deleted_node.parent)

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.min_node.value if self.size > 0 else None

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.max_node.value if self.size > 0 else None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):  # added possibility that list is empty
        return self.root.nodeToArray() if self.size > 0 else []

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.size

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        return None

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        lst = self.listToArray()
        for i in range(len(lst)):
            if lst[i] == val:
                return i
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root
