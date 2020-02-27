import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
                return
            self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
                return
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left != None:
                return self.left.contains(target)
        elif self.value <= target:
            if self.right != None:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left != None:
            self.left.for_each(cb)

        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        leftSidePrinted = False
        if node.left != None:
            leftSidePrinted = node.left.in_order_print(node.left)
        else:
            print(node.value)
            if node.right != None:
                node.right.in_order_print(node.right)
            return True
        
        if leftSidePrinted:
            print(node.value)
            if node.right != None:
                node.right.in_order_print(node.right)
            return True

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        breadthFirstQueue = Queue()
        breadthFirstQueue.enqueue(node)

        while breadthFirstQueue.size > 0:
            tempVar = breadthFirstQueue.dequeue()
            if tempVar:
                print(tempVar.value)
                if tempVar.right:
                    breadthFirstQueue.enqueue(tempVar.right)
                if tempVar.left:
                    breadthFirstQueue.enqueue(tempVar.left)

    #initialize a queue
    #push root to queue
    #while queue not empty
    #pop top item out of queue into temp var
    # this is where we do whatever with each item
    #if temp has right put into queue
    #if temp has left put into queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        if node.left != None:
            node.left.dft_print(node.left)

        if node.right != None:
            node.right.dft_print(node.right)
        #depthFirstStack = Stack(node)

        #while depthFirstStack.size > 0:
        #    tempVar = depthFirstStack.pop()
        #    print(tempVar.value)
        #    if tempVar.right:
        #        depthFirstStack.push(tempVar.right)
        #    if tempVar.left:
        #        depthFirstStack.push(tempVar.left)
            
    #initialize a stack
    #push root to stack
    #while stack not empty
    #pop top item out of stack into temp var
    # this is where we do whatever with each item
    #if temp has right put into stack
    #if temp has left put into stack
    #discard temp and pop

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left != None:
            node.left.pre_order_dft(node.left)
        if node.right != None:
            node.right.pre_order_dft(node.right)

    myStack = Stack()
    counter = 0
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left != None:
            node.left.post_order_dft(node.left)
        if node.right != None:
            node.right.post_order_dft(node.right)
        print(node.value)
