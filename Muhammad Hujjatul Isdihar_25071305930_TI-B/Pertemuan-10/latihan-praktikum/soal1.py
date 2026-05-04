class StackList:
    def __init__(self):
        self.items = [] 
    def is_empty(self):
        return (self.items) == 0
    
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Isi Stack Kosong"
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return "Isi Stack Kosong"
        return self.items[-1]
    def size(self):
        return len(self.items)

stackku = StackList()
stackku.push("A")
stackku.push("B")
stackku.push("C")

print("Stack: ", stackku.items)
print("Pop: ", stackku.pop())
print("Stack setelah di pop: ", stackku.items)
print("Peek: ", stackku.peek())
print("isEmpty: ", stackku.is_empty())
print("Size: ", stackku.size())


class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:  
    def __init__(self): 
        self.top = None
        self.count = 0 
    def is_empty(self):
        return self.count == 0
    
    def push(self, url):
        baru = Node(url)
        if self.top:
            baru.next = self.top
        self.top = baru
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Isi Stack Kosong"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url
    def peek(self):
        if self.is_empty():
            return "Isi Stack Kosong"
        return self.top.url
    
    def size(self):
        return self.count
    
myStack = StackLinkedList()
myStack.push('https://www.w3schools.com/python/python_dsa_stacks.asp')
myStack.push('https://ruang-musyawarah.web.app/')
myStack.push('https://github.com/muhammadisdihar21-ui/my-project')

print()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())