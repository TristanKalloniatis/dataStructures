class QueueNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        result = str(self.data)
        if self.prev:
            result += ". Previous: " + str(self.prev.data)
        if self.next:
            result += ". Next: " + str(self.next.data)
        return result


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = str(self.length)
        if self.head:
            result += ". Head: " + str(self.head.data)
        if self.tail:
            result += ". Tail: " + str(self.tail.data)
        return result

    def enqueue(self, data):
        new = QueueNode(data)
        if self.length > 0:
            self.tail.prev = new
            new.next = self.tail
            self.tail = new
        else:
            self.head = new
            self.tail = new
        self.length += 1
        return

    def dequeue(self):
        if self.length > 1:
            result = self.head.data
            self.head = self.head.prev
            self.head.next = None
            self.length -= 1
        elif self.length == 1:
            result = self.head.data
            self.head = None
            self.tail = None
            self.length = 0
        else:
            result = None
        return result

    @property
    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def __str__(self):
        if self.top:
            return str(self.top)
        else:
            return ""

    def push(self, data):
        new = StackNode(data)
        new.next = self.top
        self.top = new
        self.length += 1
        return

    def pop(self):
        if self.length > 1:
            result = self.top.data
            self.top = self.top.next
            self.length -= 1
            return result
        elif self.length == 1:
            result = self.top.data
            self.top = None
            self.length = 0
            return result
        else:
            return None

    @property
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        result = str(self.data)
        if self.next:
            result += ". Next: " + str(self.next.data)
        return result


class SinglyLinkedList:
    def __init__(self):
        self.start = None
        self.internalCount = 0

    def __str__(self):
        if self.start:
            return str(self.start)
        else:
            return ""

    def traverse(self):
        n = self.start
        while n:
            print(n.data)
            n = n.next
        return

    def insertRelativeToNode(self, data, node):
        new = SinglyLinkedListNode(data)
        self.internalCount += 1
        new.next = node.next
        node.next = new
        return

    def insertAtStart(self, data):
        new = SinglyLinkedListNode(data)
        self.internalCount += 1
        new.next = self.start
        self.start = new
        return

    def insertAtEnd(self, data):
        new = SinglyLinkedListNode(data)
        self.internalCount += 1
        n = self.start
        if n:
            while n.next:
                n = n.next
            n.next = new
        else:
            self.start = new
        return

    def search(self, data):
        n = self.start
        while n:
            if data == n.data:
                return True
            n = n.next
        return False

    def insertAfterElement(self, data, element):
        n = self.start
        while n:
            if element == n.data:
                break
            n = n.next
        if n:
            self.insertRelativeToNode(data, n)
        else:
            print(element, "not found")
        return

    def insertBeforeElement(self, data, element):
        n = self.start
        if n:
            if element == n.data:
                self.insertAtStart(data)
                return
            while n.next:
                if element == n.next.data:
                    break
                n = n.next
            if n.next:
                self.insertRelativeToNode(data, n)
            else:
                print(element, "not found")
        else:
            print("Empty list")
        return

    def insertAtPosition(self, data, position):
        if position == 1:
            self.insertAtStart(data)
            return
        i = 1
        n = self.start
        while i < position - 1 and n:
            n = n.next
            i = i + 1
        if n:
            self.insertRelativeToNode(data, n)
        else:
            print("List too short")
        return

    def deleteAtStart(self):
        if self.start:
            self.start = self.start.next
            self.internalCount -= 1
        else:
            print("Empty list")
        return

    def deleteAtEnd(self):
        n = self.start
        if n:
            self.internalCount -= 1
            if n.next:
                while n.next.next:
                    n = n.next
                n.next = None
            else:
                self.start = None
        else:
            print("Empty list")
        return

    def deleteByItem(self, data):
        n = self.start
        if n:
            if data == n.data:
                self.start = self.start.next
                self.internalCount -= 1
                return
            while n.next:
                if data == n.next.data:
                    break
                n = n.next
            if n.next:
                n.next = n.next.next
                self.internalCount -= 1
            else:
                print(data, "not found")
            return
        else:
            print(data, "not found")
            return

    def deleteAtPosition(self, position):
        n = self.start
        if n:
            if position == 1:
                self.deleteAtStart()
                return
            i = 1
            n = self.start
            while i < position - 1 and n.next:
                n = n.next
                i = i + 1
            if n.next:
                n.next = n.next.next
                self.internalCount -= 1
            else:
                print("List too short")
            return
        else:
            print("List too short")
            return

    def reverse(self):
        prev = None
        current = self.start
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.start = prev

    @property
    def count(self):
        total = 0
        n = self.start
        while n:
            total += 1
            n = n.next
        return total


class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        result = str(self.data)
        if self.prev:
            result += ". Previous: " + str(self.prev.data)
        if self.next:
            result += ". Next: " + str(self.next.data)
        return result


class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.internalCount = 0

    def __str__(self):
        if self.start:
            return str(self.start)
        else:
            return ""

    def traverse(self):
        n = self.start
        while n:
            print(n.data)
            n = n.next
        return

    def search(self, data):
        n = self.start
        while n:
            if data == n.data:
                return True
            n = n.next
        return False

    def insertAtStart(self, data):
        n = self.start
        new = DoublyLinkedListNode(data)
        self.internalCount += 1
        self.start = new
        if n:
            new.next = n
            n.prev = new
        return

    def insertAtEnd(self, data):
        n = self.start
        new = DoublyLinkedListNode(data)
        self.internalCount += 1
        if n:
            while n.next:
                n = n.next
            n.next = new
            new.prev = n
        else:
            self.start = new
        return

    def insertRelativeToNode(self, data, node):
        new = DoublyLinkedListNode(data)
        self.internalCount += 1
        new.next = node.next
        node.next = new
        new.prev = node
        if new.next:
            new.next.prev = new
        return

    def insertAfterElement(self, data, element):
        n = self.start
        while n:
            if element == n.data:
                break
            n = n.next
        if n:
            self.insertRelativeToNode(data, n)
        else:
            print(element, "not found")
        return

    def insertBeforeElement(self, data, element):
        n = self.start
        if n:
            if element == n.data:
                self.insertAtStart(data)
                return
            while n.next:
                if element == n.next.data:
                    break
                n = n.next
            if n.next:
                self.insertRelativeToNode(data, n)
            else:
                print(element, "not found")
        else:
            print("Empty list")
        return

    def deleteAtStart(self):
        if self.start:
            self.start = self.start.next
            self.start.prev = None
            self.internalCount -= 1
        else:
            print("Empty list")
        return

    def deleteAtEnd(self):
        n = self.start
        if n:
            self.internalCount -= 1
            while n.next:
                n = n.next
            if n.prev:
                n.prev.next = None
            else:
                self.start = None
        else:
            print("Empty list")
        return

    def deleteByItem(self, data):
        n = self.start
        if n:
            if data == n.data:
                self.deleteAtStart()
            else:
                while n:
                    if data == n.data:
                        break
                    n = n.next
                if n:
                    self.internalCount -= 1
                    n.prev.next = n.next
                    if n.next:
                        n.next.prev = n.prev
                else:
                    print(data, "not found")
        else:
            print(data, "not found")
        return

    def reverse(self):
        current = self.start
        while current:
            next = current.next
            current.prev, current.next = current.next, current.prev
            if next is None:
                self.start = current
            current = next
        return

    @property
    def count(self):
        total = 0
        n = self.start
        while n:
            total += 1
            n = n.next
        return total


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        result = "Head: " + str(self.data)
        if self.left:
            result += ". Left: " + str(self.left.data)
        if self.right:
            result += ". Right: " + str(self.right.data)
        if self.parent:
            result += ". Parent: " + str(self.parent.data)
        return result

    @property
    def depthFromHere(self):
        if self.left and self.right:
            return 1 + max(self.left.depthFromHere, self.right.depthFromHere)
        elif self.left:
            return 1 + self.left.depthFromHere
        elif self.right:
            return 1 + self.right.depthFromHere
        else:
            return 1

    @property
    def heightFromHere(self):
        numParents = 0
        parent = self.parent
        while parent:
            parent = parent.parent
            numParents += 1
        return numParents

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        else:
            return False

    def findNode(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left:
            return self.left.findNode(data)
        elif data > self.data and self.right:
            return self.right.findNode(data)
        else:
            return None

    def inNumericOrder(self, valuesSoFar):
        if self.left:
            self.left.inNumericOrder(valuesSoFar)
        valuesSoFar.append(self.data)
        if self.right:
            self.right.inNumericOrder(valuesSoFar)
        return valuesSoFar

    def insert(self, data):
        if data == self.data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BSTNode(data)
                self.left.parent = self
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = BSTNode(data)
                self.right.parent = self
                return True


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        if self.root:
            return str(self.root)
        return ""

    @property
    def depth(self):
        if self.root:
            return self.root.depthFromHere
        else:
            return 0

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    @property
    def inNumericOrder(self):
        if self.root:
            return self.root.inNumericOrder([])
        else:
            return []

    def insert(self, data):
        if self.root:
            inserted = self.root.insert(data)
            if inserted:
                self.size += 1
            return inserted
        else:
            self.root = BSTNode(data)
            self.size += 1
            return True

    def multipleInsert(self, datas):
        return [self.insert(data) for data in datas]

    def delete(self, data):
        if self.root:
            deleteNode = self.root.findNode(data)
            if deleteNode:
                self.size -= 1
                if deleteNode.left and deleteNode.right:
                    subsequentNode = deleteNode.right
                    while subsequentNode.left:
                        subsequentNode = subsequentNode.left
                    deleteNode.data = subsequentNode.data
                    if subsequentNode.data < subsequentNode.parent.data:
                        subsequentNode.parent.left = subsequentNode.right
                    else:
                        subsequentNode.parent.right = subsequentNode.right
                    if subsequentNode.right:
                        subsequentNode.right.parent = subsequentNode.parent
                elif deleteNode.left:
                    if deleteNode.parent:
                        if data < deleteNode.parent.data:
                            deleteNode.parent.left = deleteNode.left
                        else:
                            deleteNode.parent.right = deleteNode.left
                        deleteNode.left.parent = deleteNode.parent
                    else:
                        self.root = deleteNode.left
                        self.root.parent = None
                elif deleteNode.right:
                    if deleteNode.parent:
                        if data < deleteNode.parent.data:
                            deleteNode.parent.left = deleteNode.right
                        else:
                            deleteNode.parent.right = deleteNode.right
                        deleteNode.right.parent = deleteNode.parent
                    else:
                        self.root = deleteNode.right
                        self.root.parent = None
                else:
                    if deleteNode.parent:
                        if data < deleteNode.parent.data:
                            deleteNode.parent.left = None
                        else:
                            deleteNode.parent.right = None
                    else:
                        self.root = None
                return True
            else:
                return False
        else:
            return False

    def multipleDelete(self, datas):
        return [self.delete(data) for data in datas]


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        result = "Head: " + str(self.data)
        if self.left:
            result += ". Left: " + str(self.left.data)
        if self.right:
            result += ". Right: " + str(self.right.data)
        if self.parent:
            result += ". Parent: " + str(self.parent.data)
        return result

    @property
    def smallestParent(self):
        if self.parent:
            parentData = self.parent.data
            parentSmallestParent = self.parent.smallestParent
            if parentSmallestParent:
                return min(parentSmallestParent, parentData)
            else:
                return parentData
        else:
            return None

    @property
    def largestParent(self):
        if self.parent:
            parentData = self.parent.data
            parentLargestParent = self.parent.largestParent
            if parentLargestParent:
                return max(parentLargestParent, parentData)
            else:
                return parentData
        return None

    def isBSTFromHere(self, minValueAllowed, maxValueAllowed):
        if minValueAllowed and maxValueAllowed:
            if self.data < minValueAllowed or self.data > maxValueAllowed:
                return False
            if self.left and self.right:
                return self.left.isBSTFromHere(minValueAllowed, self.data - 1) and self.right.isBSTFromHere(
                    self.data + 1, maxValueAllowed)
            elif self.left:
                return self.left.isBSTFromHere(minValueAllowed, self.data - 1)
            elif self.right:
                return self.right.isBSTFromHere(self.data + 1, maxValueAllowed)
            else:
                return True
        elif minValueAllowed:
            if self.data < minValueAllowed:
                return False
            if self.left and self.right:
                return self.left.isBSTFromHere(minValueAllowed, self.data - 1) and self.right.isBSTFromHere(
                    self.data + 1, None)
            elif self.left:
                return self.left.isBSTFromHere(minValueAllowed, self.data - 1)
            elif self.right:
                return self.right.isBSTFromHere(self.data + 1, None)
            else:
                return True
        elif maxValueAllowed:
            if self.data > maxValueAllowed:
                return False
            if self.left and self.right:
                return self.left.isBSTFromHere(None, self.data - 1) and self.right.isBSTFromHere(
                    self.data + 1, maxValueAllowed)
            elif self.left:
                return self.left.isBSTFromHere(None, self.data - 1)
            elif self.right:
                return self.right.isBSTFromHere(self.data + 1, maxValueAllowed)
            else:
                return True
        else:
            if self.left and self.right:
                return self.left.isBSTFromHere(None, self.data - 1) and self.right.isBSTFromHere(
                    self.data + 1, None)
            elif self.left:
                return self.left.isBSTFromHere(None, self.data - 1)
            elif self.right:
                return self.right.isBSTFromHere(self.data + 1, None)
            else:
                return True


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        if self.root:
            return str(self.root)
        return ""

    def createRoot(self, data):
        if self.root:
            print("Root already exists with data:", self.root.data)
            return False
        else:
            self.root = BinaryTreeNode(data)
            return True

    def insert(self, data, node, position):
        if position.lower() != 'l' and position.lower() != 'r':
            print("Invalid position", position)
            return False
        new = BinaryTreeNode(data)
        self.size += 1
        new.parent = node
        if position.lower() == 'l':
            if node.left:
                node.left.parent = new
                new.left = node.left
            node.left = new
        else:
            if node.right:
                node.right.parent = new
                new.right = node.right
            node.right = new
        return True

    def delete(self, node):
        if node.left and node.right:
            print("Cannot delete unambiguously")
            return False
        elif node.left:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
            else:
                self.root = node.left
                self.root.parent = None
        elif node.right:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
            else:
                self.root = node.right
                self.root.parent = None
        else:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
        self.size -= 1
        return True

    @property
    def isBST(self):
        if self.root:
            return self.root.isBSTFromHere(None, None)
        else:
            return True
