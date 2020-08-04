# Course: CS261 - Data Structures
# Student Joel Chenoweth
# Assignment: Binary Search Tree
# Description: this is the process for coding Binary Search Tree data structure including size, height, traverse of
#parent and child nodes.


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty
    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty
    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def add(self, value: object) -> None:
        """this method adds new nodes into binary search tree w/value added"""
        #binary search tree == empty
        if self.root is None:
            self.root = TreeNode(value)
            return

        #variables loop/traverse bt
        child = self.root
        parent = None

        # place node via while loop
        while child is not None:
            parent = child
            if value < child.value:
                child = child.left
            else:
                child = child.right

        #new_node/ child
        if value < parent.value:
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)


    def contains(self, value: object) -> bool:
        """this method determines if a value is present in binary search tree searching for value and determining
        if value was found """
        # iterate tree for value
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        # value !=found thus return False
        return False


    def get_first(self) -> object:
        """this method returns the root node value stored in binary search tree"""
        #binary search tree == empty
        if self.root is None:
            return None

        # return
        return self.root.value


    def remove(self, value: object) -> bool:
        """this method removes first node returning a bool if node was removed true or false """
        # iterate tree
        left_bool = False
        node_found = False
        parent = None
        to_remove = self.root
        while to_remove is not None and not node_found:
            if value == to_remove.value:
                node_found = True
            elif value < to_remove.value:
                parent = to_remove
                to_remove = to_remove.left
                left_bool = True
            else:
                parent = to_remove
                to_remove = to_remove.right
                left_bool = False

        #value was not in binary search tree
        if not node_found:
            return False

        #node to remove is root
        if to_remove == self.root:
            self.remove_first()
            return True

        #remove is a leaf
        if self.is_leaf(to_remove) and left_bool:
            parent.left = None
            return True
        if self.is_leaf(to_remove) and not left_bool:
            parent.right = None
            return True

        #left tree
        if to_remove.right is None and left_bool:
            parent.left = to_remove.left
            return True
        if to_remove.right is None and not left_bool:
            parent.right = to_remove.left
            return True

        #right tree
        # find left-most child from right side
        left_bool_2 = False
        replace_node = to_remove.right
        replace_parent = to_remove
        while replace_node.left is not None:
            replace_parent = replace_node
            replace_node = replace_node.left
            left_bool_2 = True

        #removing new_to_remove
        if left_bool_2:
            replace_parent.left = replace_node.right
        if not left_bool_2:
            replace_parent.right = replace_node.right

        # insert left child
        if left_bool:
            parent.left = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True
        if not left_bool:
            parent.right = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True


    def remove_first(self) -> bool:
        """this removes root node from binary search tree returning a bool true/false if removed"""
        #tree isempty
        if self.root is None:
            return False

        #root== leaf
        if self.is_leaf(self.root):
            self.root = None
            return True

        #root has!= right tree
        if self.root.right is None:
            self.root = self.root.left
            return True

        #right tree
        #right tree
        replace_node = self.root.right
        replace_parent = self.root
        left_bool = False
        while replace_node.left is not None:
            replace_parent = replace_node
            replace_node = replace_node.left
            left_bool = True

        # remove left
        if left_bool:
            replace_parent.left = replace_node.right
        else:
            replace_parent.right = replace_node.right

        # insert left into root
        replace_node.left = self.root.left
        replace_node.right = self.root.right
        self.root = replace_node
        return True


    def pre_order_traversal(self) -> Queue:
        """this method inits a pre-order traversal of binary search tree returning node in order of visitation"""
        # initialize
        q = Queue()

        #binary search tree == empty
        if self.root is None:
            return q

        #recursive helper return Queue
        self.pre_order_helper(self.root, q)
        return q


    def pre_order_helper(self, node: object, q: object) -> None:
        """this recursive helper traverses current node building queue w/inputs current nde"""
        #current node
        q.enqueue(node)

        #traversal to left
        if node.left is not None:
            self.pre_order_helper(node.left, q)

        #traversal to right
        if node.right is not None:
            self.pre_order_helper(node.right, q)


    def in_order_traversal(self) -> Queue:
        """this method performs traversal of binary search tree returning queue nodes in order of visitation"""
        # initialize Queue
        q = Queue()

        #binary search tree is empty
        if self.root is None:
            return q

        #recursive helper function (non-empty)return new Queue
        self.in_order_helper(self.root, q)
        return q


    def in_order_helper(self, node: object, q: object) -> None:
        """this method is a helper function performed recursively in order to traverse node"""
        #traversal to node left
        if node.left is not None:
            self.in_order_helper(node.left, q)

        # process current node
        q.enqueue(node)

        #traversal to node right
        if node.right is not None:
            self.in_order_helper(node.right, q)


    def post_order_traversal(self) -> Queue:
        """this method is a post-order traversal binary search tree returning resulting queue"""
        # initialize Queue
        q = Queue()

        #BST == empty
        if self.root is None:
            return q

        #recursive helper function return new Queue
        self.post_order_helper(self.root, q)
        return q


    def post_order_helper(self, node: object, q: object) -> None:
        """this helper function processes post traversal object recursively"""
        #traversal to node left
        if node.left is not None:
            self.post_order_helper(node.left, q)

        #traversal to node right
        if node.right is not None:
            self.post_order_helper(node.right, q)

        #current node
        q.enqueue(node)


    def by_level_traversal(self) -> Queue:
        """this method is a traversal by-level of binary search tree returning queue containing nodes in order visited"""
        # initialize Queue objects
        new_q = Queue()
        last_q = Queue()

        #binary search tree == empty
        if self.root is None:
            return last_q

        #root in enque.q
        new_q.enqueue(self.root)

        # iterate for processing
        while not new_q.is_empty():
            working_node = new_q.dequeue()
            if working_node is not None:
                last_q.enqueue(working_node)
                new_q.enqueue(working_node.left)
                new_q.enqueue(working_node.right)

        return last_q


    def is_full(self) -> bool:
        """this method determines if the binary search tree is full returning a boolean true/false"""
        #BST == empty
        if self.root is None:
            return True

        #BST == root node
        if self.root.left is None and self.root.right is None:
            return True

        #recursive helper
        return self.is_full_helper(self.root)


    def is_full_helper(self, node: object) -> bool:
        """this method uses recursive helpers to determine if the helper is full returning a boolean true/false"""
        #node == leaf
        if self.is_leaf(node):
            return True

        #node == child
        if node.left is None and node.right is not None:
            return False
        if node.left is not None and node.right is None:
            return False

        #node == two child
        return True and self.is_full_helper(node.left) and self.is_full_helper(node.right)


    def is_complete(self) -> bool:
        """this method determines if binary search tree is complete returning a boolean true/false if such"""
        #binary search tree == empty
        if self.root is None:
            return True

        #binary search tree== perfect
        if self.is_perfect():
            return True

        #binary search tree== queue
        q = Queue()
        q.enqueue(self.root)

        #processing
        need_leaves = False
        while not q.is_empty():
            node = q.dequeue()


            if not need_leaves:
            #node left == None, node right == full
                if node.left is None and node.right is not None:
                    return False

                #node == leaf
                elif self.is_leaf(node):
                    need_leaves = True

                #node left == populated, node right == None
                elif node.left is not None and node.right is None:
                    need_leaves = True
                    q.enqueue(node.left)

                #node == two children
                if not need_leaves and node.left is not None and node.right is not None:
                    q.enqueue(node.left)
                    q.enqueue(node.right)

            # ndlves
            elif need_leaves:
                if not self.is_leaf(node):
                    return False


        return True


    def is_perfect(self) -> bool:
        """this method determines if there is a perfect binary search tree returning a boolean true/false"""
        #binary search tree==empty
        if self.root is None:
            return True

        # loop binary search tree
        height = self.height()
        return self.is_perfect_helper(self.root, 0, height)


    def is_perfect_helper(self, node: object, iter: int, iter_limit: int) -> bool:
        """this is a recursive helper to iterate current node as processed returning a boolean true/false as indicated"""
        # handle base case where iteration limit reached without returning false
        if iter == iter_limit:
            return True

        #node < 2 child
        if node.left is None or node.right is None:
            return False

        #node == 2 child
        return self.is_perfect_helper(node.left, iter + 1, iter_limit) and self.is_perfect_helper(node.right, iter + 1, iter_limit)


    def size(self) -> int:
        """this returns the number of treenodes in binary search tree"""
        #binary search tree == empty
        if self.root is None:
            return 0

        #recursive helper count nodes
        return self.size_helper(self.root)


    def size_helper(self, node: object) -> int:
        """this is a recursive helper for size of current node processed returning the nodes of binary search tree"""
        #current node
        count = 1

        # current node left
        if node.left is not None:
            count += self.size_helper(node.left)

        #current node right
        if node.right is not None:
            count += self.size_helper(node.right)

        return count


    def height(self) -> int:
        """this method returns the height of binary search tree"""
        # binary search tree == empty
        if self.root is None:
            return -1

        #count number
        return self.height_helper(self.root)


    def height_helper(self, node: object) -> int:
        """this is a helper function current node in process returning height of binary search tree """
        #current node == a leaf
        if self.is_leaf(node):
            return 0

        #current node == a single child
        if node.left is not None and node.right is None:
            return 1 + self.height_helper(node.left)
        if node.left is None and node.right is not None:
            return 1 + self.height_helper(node.right)

        #node ==2 child leaf
        if self.height_helper(node.left) > self.height_helper(node.right):
            return 1 + self.height_helper(node.left)
        else:
            return 1 + self.height_helper(node.right)


    def count_leaves(self) -> int:
        """this method counts number of nodes in binary search tree w/out child leaf returning
        nodes w/no child leaf. """
        # binary search tree == empty
        if self.root is None:
            return 0

        #recursive helper function +=count total leaf
        return self.count_leaves_helper(self.root)


    def count_leaves_helper(self, node: object) -> int:
        """this method is a helper to count child leaf of node in process returning
        leaf in binary search tree."""

        #current node == leaf
        if self.is_leaf(node):
            return 1

        # handle recursive case where current node== 1 child
        if node.left is not None and node.right is None:
            return self.count_leaves_helper(node.left)
        if node.left is None and node.right is not None:
            return self.count_leaves_helper(node.right)

        # current node == 2 child nodes
        return self.count_leaves_helper(node.left) + self.count_leaves_helper(node.right)


    def count_unique(self) -> int:
        """counts number of nodes with values to be stored in binary search tree"""
        # Binary Search Tree == empty
        if self.root is None:
            return 0

        #count values
        q = Queue()
        return self.count_unique_helper(self.root, q)


    def count_unique_helper(self, node: object, q: object) -> int:
        """this method is a helper(recursion sort) for node in current process with objects
        added with unique values from binary search tree returning values into binary search tree"""
        # iterate/determine node.value exists within q
        temp_q = Queue()
        new_value = True
        while not q.is_empty() and new_value:
            curr_node = q.dequeue()
            temp_q.enqueue(curr_node)
            if node.value == curr_node.value:
                new_value = False

        # enqueue nodes
        while not temp_q.is_empty():
            curr_node = temp_q.dequeue()
            q.enqueue(curr_node)

        #current node to convenient variable
        curr_add = 0
        if new_value:
            q.enqueue(node)
            curr_add = 1

        #current node == leaf
        if self.is_leaf(node):
            return curr_add

        #current node == single child
        if node.left is not None and node.right is None:
            return curr_add + self.count_unique_helper(node.left, q)
        if node.left is None and node.right is not None:
            return curr_add + self.count_unique_helper(node.right, q)

        #current node == 2 child nodes
        return curr_add + self.count_unique_helper(node.left, q) + self.count_unique_helper(node.right, q)


    def is_root(self, node: object) -> bool:
        """this method determines if a treenode which has passed args is a root node """
        if node == self.root:
            return True
        else:
            return False

    def is_leaf(self, node: object) -> bool:
        """this method will determine a treenode which has passed args is a leaf node"""
        if node.left == None and node.right == None:
            return True
        else:
            return False


