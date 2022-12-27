# username -
# id1      -
# name1    -
# id2      -
# name2    -

import random

"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str | None
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
            self.left.parent = self     # added
            self.right = AVLNode(None)
            self.right.parent = self    # added
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
        return self.value is not None   # added not - not None --> real node

    """returns an array containing all 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """

    def nodeToArray(self):
        left_node_array = self.getLeft().nodeToArray() if self.getLeft().isRealNode() else []
        right_node_array = self.getRight().nodeToArray() if self.getRight().isRealNode() else []
        self_array = [self.value] if self.isRealNode() else []  # added in case node is virtual
        return left_node_array + self_array + right_node_array

    """fixes fields of a node to a correct size after rotations
        
        @pre: node.left.size and node.right.size are correct
        @pre: node.left.height and node.right.height are correct
    """

    def update(self):
        self.size = self.left.size + self.right.size + 1
        self.height = max(self.left.height, self.right.height) + 1

    """fixes fields of a node to a correct size after rotations

            @pre: node.left.size and node.right.size are correct
            @pre: node.left.height and node.right.height are correct
        """

    def successor(self):
        if self.getRight().isRealNode():
            to_return = self.getRight()
            while to_return.getLeft().isRealNode():
                to_return = to_return.getLeft()
        else:
            tmp = self
            while tmp.getParent() is not None and tmp.getParent().getRight() == tmp:
                tmp = tmp.getParent()
            to_return = tmp.getParent()
        return to_return


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
        if self.root is None or i < 0 or i >= self.root.size:   # added possibility that the tree is empty
            print("CANNOT SEARCH FOR", i, "IN THE TREE")
            print(self.size)
            return None
        if i == 0:
            return self.min_node
        # if i == self.size - 1:    # using retrieve_node to fix max_node; screws it up
        #     return self.max_node
        pointer_node = self.min_node
        new_index = i
        while pointer_node.size <= i:
            pointer_node = pointer_node.parent
        while new_index != pointer_node.getLeft().size:
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

    def retrieve(self, i):  # added possibility the index was invalid
        node = self.retrieve_node(i)
        return node.value if node is not None else None

    """Does maintenance for swapped nodes in LL/RR rotations

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: str
        @returns: the the value of the i'th item in the list
        """

    def rotation_fixes(self, subtree, node, decreasing_node):
        subtree.setParent(decreasing_node)
        if decreasing_node.parent is not None:
            if decreasing_node.parent.getLeft() == decreasing_node:
                decreasing_node.parent.setLeft(node)
            else:
                decreasing_node.parent.setRight(node)
        node.setParent(decreasing_node.parent)
        # fixes the parental connection to the swapped nodes
        decreasing_node.setParent(node)
        if self.root == decreasing_node:
            self.root = node
        # maintain height and size
        decreasing_node.update()
        node.update()
        return 1

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
        return self.rotation_fixes(subtree, node, decreasing_node)

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
        return self.rotation_fixes(subtree, node, decreasing_node)

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
            node.update()
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
            subtree = AVLNode(None)
            if r_l_flag == 'R':
                subtree = parent_node.right
                parent_node.right = son
                son.right = subtree
            if r_l_flag == 'L':
                subtree = parent_node.left
                parent_node.left = son
                son.left = subtree
            son.parent = parent_node
            subtree.parent = son    # happens even is subtree is not real
            # fix height, size
            son.update()
            parent_node.update()

        new_node = AVLNode(val)
        # take care of empty tree
        if self.size == 0:
            self.root = self.min_node = self.max_node = new_node
            to_return = self.maintain(new_node)
            return to_return if to_return is not None else 0
        if i == 0:
            inner_insert(self.min_node, new_node, 'L')
            self.min_node = new_node
        elif i == self.size:
            inner_insert(self.max_node, new_node, 'R')
            self.max_node = new_node
        else:
            next_node = self.retrieve_node(i)   # fixed to i instead of i+1
            if next_node.left.value is None:
                inner_insert(next_node, new_node, 'L')  # fixed to next node instead of new node
            else:
                prev_node = self.retrieve_node(i - 1)
                inner_insert(prev_node, new_node, 'R')
        # fix AVL invariant
        to_return = self.maintain(new_node.parent)
        return to_return if to_return is not None else 0

    """deletes the given node from the AVLTree. 

    @param node: The intended node in the AVLTree to be deleted
    @rtype: AVLNode
    @returns: the closest node to the deleted node: if deleted node had a son -> son, if deleted node was a leaf -> parent 
    """

    # OMER - IT DOES NOT MAINTAIN AVL INVARIANT, NOTICE WHILE USING
    def delete_node(self, node):
        # maintain min_node, max_node
        if node == self.min_node:
            self.min_node = self.min_node.right if self.min_node.right.isRealNode() else self.min_node.parent  # changed
        if node == self.max_node:
            self.max_node = self.retrieve_node(self.size - 2)
        # takes care of node with 2 children
        if node.left.value is not None and node.right.value is not None:
            successor = node.successor()
            node.value = successor.value
            node = successor
            return self.delete_node(node)   # as a return
        # actually delete
        node.right.parent = node.parent
        node.left.parent = node.parent
        if node.left.value is None:  # has only right son or no sons at all
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.parent.update()
            if node.right.value is not None:    # deleted node has a right child
                return node.right
            else:   # deleted node had no children
                return node.parent
        else:  # has only left son
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.parent.update()
            return node.left

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
            self.__init__()
            return 0
        # perform a regular deletion
        deleted_node = self.retrieve_node(i)
        near_deleted_node = self.delete_node(deleted_node)
        # fix AVL invariant & AVLTree fields - moved min-max maintaining into maintain
        return self.maintain(near_deleted_node)

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

    def listToArray(self):  # added possibility that list is empty so root is None
        return self.root.nodeToArray() if self.root is not None else []

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
        def merge_sort(array):
            def merge(arr1, arr2):
                merged_arr = []
                i = j = 0
                while i < len(arr1) or j < len(arr2):
                    if i >= len(arr1) or (j < len(arr2) and arr2[j] < arr1[i]):
                        merged_arr.append(arr2[j])
                        j += 1
                    else:
                        merged_arr.append(arr1[i])
                        i += 1
                return merged_arr

            if len(array) > 1:
                mid = len(array) // 2
                left = array[:mid]
                right = array[mid:]
                return merge(merge_sort(left), merge_sort(right))
            return array

        arr = self.listToArray()
        sorted_arr = merge_sort(arr)
        return arrayToTree(sorted_arr)

    def append(self, val):
        return self.insert(self.length(), val)

    def getTreeHeight(self):
        return self.root.height

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list.
    """

    def permutation(self):
        def shuffle(array):
            end = len(array) - 1
            while end > 0:
                i = random.randint(0, end)
                value = array[i]
                array[i] = array[end]
                array[end] = value
                end -= 1

        arr = self.listToArray()
        shuffle(arr)
        return arrayToTree(arr)

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        former_height = self.getRoot().height if self.getRoot() is not None else -1
        former_size = self.getRoot().size if self.getRoot() is not None else 0
        lst_height = lst.getRoot().height if lst.getRoot() is not None else -1
        lst_size = lst.getRoot().size  if lst.getRoot() is not None else 0
        if lst_size == 0:
            return max(former_height, 0)
        if former_size == 0:
            self.root = lst.root
            self.size = lst.size
            self.min_node = lst.min_node
            self.max_node = lst.max_node
            return max(lst_height, 0)
        temp_node = AVLNode("0")
        if lst_height > former_height - 1:
            node = lst.getRoot()
            while node.height > former_height + 1:
                node = node.getLeft()
            temp_node.setParent(node)
            temp_node.setLeft(self.root)
            temp_node.getLeft().setParent(temp_node)
            temp_node.setRight(node.getLeft())
            temp_node.getRight().setParent(temp_node)
            temp_node.update()
            node.setLeft(temp_node)
            node.update()
            while node.getParent() is not None:
                node = node.getParent()
                node.update()
            self.root = node
        elif lst_height < former_height - 1:
            node = self.getRoot()
            while node.height > lst_height + 1:
                node = node.getRight()
            temp_node.setParent(node)
            temp_node.setRight(node.getLeft())
            temp_node.getRight().setParent(temp_node)
            temp_node.setLeft(node.getLeft())
            temp_node.getLeft().setParent(temp_node)
            temp_node.update()
            node.setLeft(temp_node)
            node.update()
            while node.getParent() is not None:
                node = node.getParent()
                node.update()
        else:
            temp_node.setLeft(self.getRoot())
            temp_node.getLeft().setParent(temp_node)
            temp_node.setRight(lst.getRoot())
            temp_node.getRight().setParent(temp_node)
            temp_node.update()
            self.root = temp_node

        self.size = self.root.size
        self.max_node = lst.max_node
        self.delete(former_size)

        return abs(max(former_height, 0) - max(lst_height, 0))

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        lst = self.listToArray()  # O(n)
        for i in range(len(lst)):   # the total complexity is already O(n)
            if lst[i] == val:
                return i
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root

    def printt(self):
        out = ""
        for row in self.printree(self.root):  # need printree.py file
            out = out + row + "\n"
        print(out)

    def printree(self, t, bykey=True):
        # for row in trepr(t, bykey):
        #        print(row)
        return self.trepr(t, False)

    def trepr(self, t, bykey=False):
        if t == None:
            return ["#"]

        thistr = str(t.key) if bykey else str(t.getValue())

        return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

    def conc(self, left, root, right):

        lwid = len(left[-1])
        rwid = len(right[-1])
        rootwid = len(root)

        result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

        ls = self.leftspace(left[0])
        rs = self.rightspace(right[0])
        result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
                      " " + "\\" + rs * "_" + (rwid - rs) * " ")

        for i in range(max(len(left), len(right))):
            row = ""
            if i < len(left):
                row += left[i]
            else:
                row += lwid * " "

            row += (rootwid + 2) * " "

            if i < len(right):
                row += right[i]
            else:
                row += rwid * " "

            result.append(row)

        return result

    def leftspace(self, row):
        # row is the first row of a left node
        # returns the index of where the second whitespace starts
        i = len(row) - 1
        while row[i] == " ":
            i -= 1
        return i + 1

    def rightspace(self, row):
        # row is the first row of a right node
        # returns the index of where the first whitespace ends
        i = 0
        while row[i] == " ":
            i += 1
        return i


"""returns an AVLTreeList representing an array given as a python list

@rtype: AVLTreeList
@returns: an AVLTreeList of strings representing the given list
"""


def arrayToTree(arr):
    tree = AVLTreeList()
    tree.root = arrayToTreeRec(arr)
    tree.size = tree.root.size
    pointer = tree.root
    while pointer.left.isRealNode():
        pointer = pointer.left
    tree.min_node = pointer
    pointer = tree.root
    while pointer.right.isRealNode():
        pointer = pointer.right
    tree.max_node = pointer
    return tree


"""returns an AVLNode which is the root of an AVLTreeList representing arr

@rtype: AVLNode
@returns: an AVLNode which is root of tree of strings representing the given list
"""


def arrayToTreeRec(arr):
    mid_loc = len(arr) // 2
    mid_node = AVLNode(arr[mid_loc])
    right_node = arrayToTreeRec(arr[mid_loc + 1:]) if len(arr) - mid_loc - 1 > 0 else AVLNode(None)
    left_node = arrayToTreeRec(arr[:mid_loc]) if mid_loc > 0 else AVLNode(None)
    mid_node.right = right_node
    right_node.parent = mid_node
    mid_node.left = left_node
    left_node.parent = mid_node
    mid_node.update()
    return mid_node


def test():
    T1 = AVLTreeList()
    T2 = AVLTreeList()
    L1 = list()
    L2 = list()
    for i in range(10):
        T1.append(i)
        L1.append(i)
    for i in range(5):
        T2.append(i)
        L2.append(i)
    T1.concat(T2)
    L3 = L1 + L2
    print(T1.listToArray())
    print(L3)


if __name__ == '__main__':
    test()
