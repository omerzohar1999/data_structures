# username -
# id1      -
# name1    -
# id2      -
# name2    -


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
        self.height = -1  # Balance factor
        self.size = 1

        if value is not None:
            self.left = AVLNode(None)
            self.right = AVLNode(None)

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

    """Does an RL rotation

        @type node: AVLNode
        @pre: 0 <= search(node) < self.length()
        @param node: node in the tree
        @rtype: int
        @returns: The number of rotations - 2
        """

    def RL(self, node):
        return 2

    """Does an LR rotation

            @type node: AVLNode
            @pre: 0 <= search(node) < self.length()
            @param node: node in the tree
            @rtype: int
            @returns: The number of rotations - 2
            """

    def LR(self, node):
        return 2

    """Does an RR rotation

            @type node: AVLNode
            @pre: 0 <= search(node) < self.length()
            @param node: node in the tree
            @rtype: int
            @returns: The number of rotations - 1
            """

    def RR(self, node):
        return 1

    """Does an LL rotation

            @type node: AVLNode
            @pre: 0 <= search(node) < self.length()
            @param node: node in the tree
            @rtype: int
            @returns: The number of rotations - 1
            """

    def LL(self, node):
        return 2

    """Determines which rotation is needed and does that

                @type node: AVLNode
                @pre: 0 <= search(node) < self.length()
                @param node: node in the tree
                @rtype: int
                @returns: The number of rotations - 2
                """

    def rotate(self, node):
        return 1

    """Maintains AVL rules and node/tree fields.

    @type node: AVLNode
    @pre: 0 <= search(node) < self.length()
    @param node: node in the tree
    @rtype: int
    @returns: The number of rotations
    """

    def maintain(self, node):
        return 1

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
        # insert new node in place
        new_i_node = AVLNode(val)
        current_i_node = self.retrieve_node(i)
        current_i_node_left = current_i_node.left
        current_i_node.setLeft(new_i_node)
        new_i_node.setParent(current_i_node)
        new_i_node.setLeft(current_i_node_left)
        # fix size
        current_i_node.setSize(current_i_node.getSize()+1)
        new_i_node.setSize(current_i_node_left.getSize()+1)
        # fix height
        new_i_node.setHeight(current_i_node_left.getHeight()+1)
        current_i_node.setHeight(max(current_i_node.right.getHeight(),new_i_node.getHeight()))
        # fix min, max node
        if i == 0:
            self.min_node = new_i_node
        if i == self.size:
            self.min_node = new_i_node
        # fix AVL invariant
        return -1

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        return -1

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

    def listToArray(self):
        return self.root.nodeToArray()

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
