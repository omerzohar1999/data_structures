import random


"""A class representing a node in a linked list"""


class LLNode:
    """
    Constructor
        Complexity: O(1)

    @type value: str | None | else
    @param value: data of your node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    """
    Returns the next node
        Complexity O(1)
    
    @rtype: LLNode | None
    @returns: The next node if there is one, None else
    """
    def get_next(self):
        return self.next

    """
    Returns the node's value
        Complexity O(1)

    @rtype: str| None | else
    @returns: The next node if there is one, None else
    """
    def get_value(self):
        return self.value

    """
    sets the node's next node
        Complexity O(1)

    @type node: LLnode
    @param node: the node to become this node's next
    """
    def set_next(self, node):
        self.next = node

    """
    sets the node's value
        Complexity O(1)

    @type value: str | None | else
    @param node: the value to insert to this node
        """
    def set_value(self, value):
        self.value = value


"""A class representing a linked list"""


class LinkedList:
    """
    Constructor
        Complexity: O(1)

    @type value: str | None | else
    @param value: data of your node
    """
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    """
    adds a value at the beginning of the list
        Complexity O(1) - no recursion or loops, all actions are constant time

    @type value: str | None | else
    @param node: the value to insert at the list's beginning
    """
    def insert_first(self, value):
        to_insert = LLNode(value)
        if self.size == 0:
            self.first = self.last = to_insert
        else:
            to_insert.set_next(self.first)
            self.first = to_insert
        self.size += 1

    """
    adds a value at the end of the list
        Complexity O(1) - no recursion or loops, all actions are constant time

    @type value: str | None | else
    @param node: the value to insert at the list's end
    """
    def insert_last(self, value):
        to_insert = LLNode(value)
        if self.size == 0:
            self.first = self.last = to_insert
        else:
            self.last.set_next(to_insert)
            self.last = to_insert
        self.size += 1

    """
    adds all values from another list at the end of this one
        Complexity O(1) - no recursion or loops, all actions are constant time

    @type ll: LinkedList
    @param ll: the list to concatenate to self
    """
    def concat(self, ll):
        if self.size == 0:
            self = ll
        elif ll.size > 0:
            self.last.set_next(ll.first)
            self.last = ll.last
            self.size += ll.size

    """
    Outputs an array containing the list's values by their order
        Complexity O(n) - iterating once per list node

    @rtype: lst
    @returns: an array in which arr[i] is the value of the i'th node in the list
    """
    def to_arr(self):
        pointer = self.first
        arr = []
        while pointer is not None:
            arr.append(pointer.value)
            pointer = pointer.get_next()
        return arr


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor
        Complexity: O(1)

    @type value: str | None | else
    @param value: data of your node
    """

    def __init__(self, value, is_real=True):
        self.is_real = is_real
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

        if is_real:
            self.left = AVLNode(None, is_real=False)
            self.left.parent = self
            self.right = AVLNode(None, is_real=False)
            self.right.parent = self
            self.height = 0  # as a leaf
            self.size = 1

    """returns the left child node
        Complexity: O(1)
    @rtype: AVLNode
    @returns: the left child of self
    """

    def getLeftNode(self):
        return self.left

    """returns the right child
        Complexity: O(1)

    @rtype: AVLNode
    @returns: the right child of self
    """

    def getRightNode(self):
        return self.right

    """returns the parent 
        Complexity: O(1)

    @rtype: AVLNode
    @returns: the parent of self
    """

    def getParentNode(self):
        return self.parent

    """returns the left child
        Complexity: O(1)
        
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child
        """

    def getLeft(self):
        return self.left if self.left is not None and self.left.isRealNode() else None

    """returns the right child
    Complexity: O(1)

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right if self.right is not None and self.right.isRealNode() else None

    """returns the parent 
        Complexity: O(1)

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent if self.parent is not None and self.parent.isRealNode() else None

    """return the value
        Complexity: O(1)

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value if self.isRealNode() else None

    """returns the height
        Complexity: O(1)

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    """returns the size
        Complexity: O(1)

    @rtype: int
    @returns: the size of self
    """

    def getSize(self):
        return self.size

    """returns the Balance Factor
        Complexity: O(1)
    
    @rtype: int
    @returns: the height of left - the height of right
    """

    def getBF(self):
        if self.left is None:
            self.left = AVLNode(None, False)
        if self.right is None:
            self.right = AVLNode(None, False)
        return self.left.getHeight() - self.right.getHeight()

    """sets left child
        Complexity: O(1)

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child
        Complexity: O(1)

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent node
        Complexity: O(1)

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value to node
        Complexity: O(1)

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the node's height   
        Complexity: O(1)

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """sets the node's size
        Complexity: O(1)

    @type s: int
    @param s: the size
    """

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 
        Complexity: O(1)

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.is_real

    """returns an array containing all elements in this node's subtree.
    Complexity is O(n):
        each node is inserted once - all-in-all O(n) insertions
        arrays are then connected in doubles - right and left sub-arrays, meaning O(log(n)) connections, each is O(1)
        all-in-all O(n+log(n)) = O(n) 

    @rtype: list
    @returns: array containing all subelements of this node.
    """

    def nodeToLinkedList(self):  # Recursive, but all-in-all O(n), since we insert each node once
        left_node_list = self.getLeftNode().nodeToLinkedList() if self.getLeftNode().isRealNode() else LinkedList()
        right_node_list = self.getRightNode().nodeToLinkedList() if self.getRightNode().isRealNode() else LinkedList()
        if self.isRealNode():
            left_node_list.insert_last(self.value)
        left_node_list.concat(right_node_list)
        return left_node_list

    """fixes fields of a node to a correct size after rotations
        Complexity: O(1)
        
    @pre: node.left.size and node.right.size are correct
    @pre: node.left.height and node.right.height are correct
    """

    def update(self):
        self.size = self.left.size + self.right.size + 1
        self.height = max(self.left.height, self.right.height) + 1

    """finds node containing the successor, according to the method learned in class.
    Complexity is O(h)=O(log_2(n)) as we analyzed in class.

    @pre: node is not max in its tree
    """

    def successor(self):
        if self.getRightNode().isRealNode():
            to_return = self.getRightNode()
            while to_return.getLeftNode().isRealNode():
                to_return = to_return.getLeftNode()
        else:
            tmp = self
            while tmp.getParentNode() is not None and tmp.getParentNode().getRightNode() == tmp:
                tmp = tmp.getParentNode()
            to_return = tmp.getParentNode()
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
        self.first_node = None
        self.last_node = None

    """returns whether the list is empty
        Complexity: O(1)

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.size == 0

    """retrieves the node containing the i'th item in the list, similar to finger tree we learned in class.
    Its complexity is O(log_2(i)) as we've seen in class.

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: AVLNode
    @returns: the node containing the i'th item in the list
    """

    def retrieve_node(self, i):
        if i == 0:
            return self.first_node  # to allow instant access
        pointer_node = self.first_node
        new_index = i  # index to look for in current subtree
        while pointer_node.size <= i:  # while my subtree still doesn't have i elements...
            pointer_node = pointer_node.parent  # go to parent for a larger subtree.
        while new_index != pointer_node.getLeftNode().size:  # then binary search on node rank.
            if pointer_node.getLeftNode().size < new_index:  # if my left subtree has less elements than new_index...
                new_index -= (pointer_node.getLeftNode().size + 1)  # its in the right subtree, but in a smaller rank.
                pointer_node = pointer_node.getRightNode()
            else:
                pointer_node = pointer_node.getLeftNode()
        return pointer_node

    """retrieves the value of the i'th item in the list
        Complexity: O(log_2(n)) using retrieve_node

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        node = self.retrieve_node(i)
        return node.value

    """Does maintenance for swapped nodes in LL/RR rotations
        Complexity: O(1)

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def rotation_fixes(self, subtree, node, decreasing_node):
        # fixes the parental connection to the swapped nodes
        subtree.setParent(decreasing_node)
        if decreasing_node.parent is not None:
            if decreasing_node.parent.getLeftNode() == decreasing_node:
                decreasing_node.parent.setLeft(node)
            else:
                decreasing_node.parent.setRight(node)
        node.setParent(decreasing_node.parent)
        decreasing_node.setParent(node)
        # maintain root
        if self.root == decreasing_node:
            self.root = node
        # maintain height and size
        decreasing_node.update()
        node.update()
        return 1

    """Does an RR rotation
        Complexity: O(1)

    @type node: AVLNode
    @pre: 0 <= search(node) < self.length()
    @pre: self.root == node -> node.getRight() is not None
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
        Complexity: O(1)

    @type node: AVLNode
    @pre: 0 <= search(node) < self.length()
    @pre: self.root == node -> node.getLeft() is not None
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
        Complexity: O(1)

    @type node: AVLNode
    @pre: 0 <= search(node) < self.length()
    @param node: node in the tree
    @rtype: int
    @returns: The number of rotations - 2
    """

    def RL(self, node):
        return self.RR(node) + self.LL(node)

    """Does an LR rotation
        Complexity: O(1)

    @type node: AVLNode
    @pre: 0 <= search(node) < self.length()
    @param node: node in the tree
    @rtype: int
    @returns: The number of rotations - 2
    """

    def LR(self, node):
        return self.LL(node) + self.RR(node)

    """Determines which rotation is needed (if needed) and does that
        Complexity: O(1)

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
        Complexity: O(log_2(n)) as learned in class

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
        Complexity: O(log_2(n)) as learned in class

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
            subtree = AVLNode(None, is_real=False)
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
            self.root = self.first_node = self.last_node = new_node
            to_return = self.maintain(new_node)
            return to_return if to_return is not None else 0
        if i == 0:
            inner_insert(self.first_node, new_node, 'L')
            self.first_node = new_node
        elif i == self.size:
            inner_insert(self.last_node, new_node, 'R')
            self.last_node = new_node
        else:
            next_node = self.retrieve_node(i)   # fixed to i instead of i+1
            if not next_node.left.isRealNode():
                inner_insert(next_node, new_node, 'L')  # fixed to next node instead of new node
            else:
                prev_node = self.retrieve_node(i - 1)
                inner_insert(prev_node, new_node, 'R')
        # fix AVL invariant
        to_return = self.maintain(new_node.parent)
        return to_return if to_return is not None else 0

    """deletes the given node from the AVLTree. 
        Complexity: O(log_2(n)) at worst case by using successor function

    @param node: The intended node in the AVLTree to be deleted
    @rtype: AVLNode
    @returns: the closest node to the deleted node: if deleted node had a son -> son, if deleted node was a leaf -> parent 
    """
    def delete_node(self, node):
        # maintain min_node, max_node
        if node == self.first_node:
            self.first_node = self.first_node.right if self.first_node.right.isRealNode() else self.first_node.parent
        if node == self.last_node:
            self.last_node = self.retrieve_node(self.size - 2)
        # takes care of node with 2 children
        if node.left.isRealNode() and node.right.isRealNode():
            successor = node.successor()
            node.value = successor.value
            node = successor
            return self.delete_node(node)
        # actually delete
        node.right.parent = node.parent
        node.left.parent = node.parent
        if not node.left.isRealNode():  # has only right son or no sons at all
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.parent.update()
            if node.right.isRealNode():    # deleted node has a right child
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
        Complexity: O(log_2(n)) as learned in class

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
        # fix AVL invariant & AVLTree fields
        return self.maintain(near_deleted_node)

    """returns the value of the first item in the list
        Complexity: O(1)

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.first_node.value if self.size > 0 else None

    """returns the value of the last item in the list
        Complexity: O(1)

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.last_node.value if self.size > 0 else None

    """returns an array representing list 
        Complexity: O(n) using AVLNode.nodeToArray method

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return self.root.nodeToLinkedList().to_arr() if self.root is not None else []  # Two O(n) actions hence O(n)



    """returns the size of the list 
        Complexity: O(1) 
        
    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.size

    """sort the info values of the list
        Complexity: O(n*log_2(n))

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        def merge_sort(array):  # O(nlogn) according to Extended Intro To Computer Science
            def merge(arr1, arr2):
                merged_arr = []
                i = j = 0
                while i < len(arr1) or j < len(arr2):
                    # Thanks to "node value can be None", this line might fail. However, it would fail on any DS,
                    # as None cannot be compared with str..
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

        arr = self.listToArray()  # O(n)
        sorted_arr = merge_sort(arr)  # O(nlogn)
        return arrayToTree(sorted_arr)  # O(n)

    def append(self, val):
        return self.insert(self.length(), val)

    def getTreeHeight(self):
        return self.root.height

    """permute the info values of the list
        Complexity: O(n) as described in documentation 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list.
    """

    def permutation(self):
        def shuffle(array):
            end = len(array) - 1
            while end > 0:  # O(n) since everything inside happens in constant time, end decrements from n to 0.
                i = random.randint(0, end)
                value = array[i]
                array[i] = array[end]
                array[end] = value
                end -= 1

        # create array using listToArray, shuffle it, then create a tree out of it using arrayToTree.
        arr = self.listToArray()  # O(n)
        shuffle(arr)  # O(n)
        return arrayToTree(arr)  # O(n)

    """concatenates lst to self
        Complexity: O(|self.getHeight() - lst.getHeight()|) as learned in class

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        # save heights and sizes for both trees in order to determine where to start
        former_height = self.getRoot().height if self.getRoot() is not None else -1
        former_size = self.getRoot().size if self.getRoot() is not None else 0
        lst_height = lst.getRoot().height if lst.getRoot() is not None else -1
        lst_size = lst.getRoot().size if lst.getRoot() is not None else 0
        # added an empty list - nothing should happen
        if lst_size == 0:
            return max(former_height, 0)
        # this list is empty - it is the same as reassigning lst to it
        if former_size == 0:
            self.root = lst.root
            self.size = lst.size
            self.first_node = lst.first_node
            self.last_node = lst.last_node
            return max(lst_height, 0)
        # create a temporary node which will be "x" in "join(T1, x, T2). we delete it in the end
        temp_node = AVLNode("0")
        if lst_height > former_height - 1:
            # self should become a left subtree of lst
            node = lst.getRoot()
            # find where to insert temp_node
            while node.height > former_height + 1:
                node = node.getLeftNode()
            # connect temp_node like "x" in AVLTree.Join(T1, x, T2). maintain node fields.
            temp_node.setParent(node)
            temp_node.setLeft(self.root)
            temp_node.getLeftNode().setParent(temp_node)
            temp_node.setRight(node.getLeftNode())
            temp_node.getRightNode().setParent(temp_node)
            temp_node.update()
            node.setLeft(temp_node)
            node.update()
            # maintain node fields all the way up to the root.
            while node.getParentNode() is not None:
                node = node.getParentNode()
                node.update()
            self.root = node

        elif lst_height < former_height - 1:
            # lst shoud become a right subtree in self
            node = self.getRoot()
            # find where to insert temp_node
            while node.height > lst_height + 1:
                node = node.getRightNode()
            # connect temp_node like "x" in AVLTree.Join(T1, x, T2). maintain node fields.
            temp_node.setParent(node)
            temp_node.setRight(node.getLeftNode())
            temp_node.getRightNode().setParent(temp_node)
            temp_node.setLeft(node.getLeftNode())
            temp_node.getLeftNode().setParent(temp_node)
            temp_node.update()
            node.setLeft(temp_node)
            node.update()
            # maintain node fields all the way up to the root.
            while node.getParentNode() is not None:
                node = node.getParentNode()
                node.update()
        else:
            # trees are of somewhat same height, so they just become left and right subtrees of temp_node.
            temp_node.setLeft(self.getRoot())
            temp_node.getLeftNode().setParent(temp_node)
            temp_node.setRight(lst.getRoot())
            temp_node.getRightNode().setParent(temp_node)
            temp_node.update()
            self.root = temp_node
        # maintain tree fields then delete temp_node.
        # it is in index former_size since it is the first item after self.
        self.size = self.root.size
        self.last_node = lst.last_node
        self.delete(former_size)
        # this calculation is thanks to the fun return value cases defined in forum.
        return abs(max(former_height, 0) - max(lst_height, 0))

    """searches for a *value* in the list
        Complexity: O(n)

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        lst = self.listToArray()  # O(n)
        for i in range(len(lst)):   # w.c O(n), b.c O(1)
            if lst[i] == val:
                return i
        return -1

    """returns the root of the tree representing the list
        Complexity: O(1)

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root


"""returns an AVLTreeList representing an array given as a python list
    Complexity: O(n) using arrayToTreeRec method 

@rtype: AVLTreeList
@returns: an AVLTreeList of strings representing the given list
"""


def arrayToTree(arr):
    tree = AVLTreeList()
    # Create root of tree which has all nodes under it
    tree.root = arrayToTreeRec(arr)
    # Update tree fields: size
    tree.size = tree.root.size
    # Update tree fields: first_node
    pointer = tree.root
    while pointer.left.isRealNode():
        pointer = pointer.left
    tree.first_node = pointer
    # Update tree fields: last_node
    pointer = tree.root
    while pointer.right.isRealNode():
        pointer = pointer.right
    tree.last_node = pointer

    return tree


"""returns an AVLNode which is the root of an AVLTreeList representing arr
    Complexity: O(n) as described in documentation

@rtype: AVLNode
@returns: an AVLNode which is root of tree of strings representing the given list
"""


def arrayToTreeRec(arr):
    # Take the middle array member and turn it into a node
    mid_loc = len(arr) // 2
    mid_node = AVLNode(arr[mid_loc])
    # recursively create AVL tree roots for the right and left subtrees
    right_node = arrayToTreeRec(arr[mid_loc + 1:]) if (len(arr) - mid_loc >= 0) else AVLNode(None, False)
    left_node = arrayToTreeRec(arr[:mid_loc]) if mid_loc > 0 else AVLNode(None, False)
    # connect node with right and left subtrees
    mid_node.right = right_node
    right_node.parent = mid_node
    mid_node.left = left_node
    left_node.parent = mid_node
    mid_node.update()
    return mid_node
