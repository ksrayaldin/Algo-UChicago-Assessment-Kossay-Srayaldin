# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

'''
Class: Node
Creates an object with two arguments: "value" and "next". It defaults the next argument to "None".
It requires the user to input a numeric value.
'''
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

'''
Class: Stack
Creates a linked list of Node objects. It initially sets the "top" of the stack to be None
'''
class Stack():
    def __init__(self):
        self.top = None
        # self.node = Node(value)

    # Every time you push, you change the value on top.
    def push(self, value):
        if (self.top is None):
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top # New node points to the previous top. Necessary for pop method
            self.top = new_node
    
    # Take out the value on the top of the stack, replace top with the object below it.
    def pop(self):
        if (self.top is None):
            raise Exception("Stack is empty! (pop)")
        else:
            value = self.top.value
            self.top = self.top.next
            return value
    
    # Return the value of the element on top
    def peek(self):
        if (self.top is None):
            raise Exception("Stack is empty! (peek)")
        return self.top.value
    
    # Iterate through stack to find current size
    def size(self):
        current = self.top
        count = 0
        if current is None:
            return count
        
        while (current is not None):
            count += 1
            current = current.next
        return count


# Testing...
# Create an empty stack: (returns nothing)
print("Creating empty stack... \n")
stack = Stack()

# Add some values to the stack 
stack.push(10)
stack.push(20)
stack.push(30)

# Find the size of the stack:
size = stack.size()
print(f"Stack is populated by {size} values (should be 3). It looks like: 30 -> 20 -> 10 \n")

# Peek at the value on top:
value = stack.peek()
print(f"value on top is {value} (should be 30)\n")

# Pop values:
value = stack.pop()
print(f"The value popped is {value} (should be 30)\n")
value = stack.pop()
print(f"The value popped is {value} (should be 20)\n")
value = stack.pop()
print(f"The value popped is {value} (should be 10)\n")

# Running pop or peek command should give an error. To test pop(), comment out peek(). To test peek(),
# comment out pop()
print(f"Running pop or peek command one more time should give an error:\n")
# value = stack.pop()
value = stack.peek()