
class OnStack:
    """Defines a stack element class implemented as a linked list node."""

    def __init__(self, data, lower=None):
        """Each element has two attributes: 'data' and 'lower',
        where 'lower' points to the next element."""
        self.data = data
        self.lower = lower

    def push(self, value):
        """At stack element level this function returns a new element
        pointing to the current one."""
        return OnStack(value, self)

    
class Stack:
    """Composite class of 'OnStack' where methods are defined."""
    
    def __init__(self):
        """The one attribute 'top' points to the last element of the
        stack."""
        self.top = None
    
    @property 
    def check_empty(self):
        """This property is required for other stack methods."""
        return self.top is None

    def push(self, value):
        """Here a value is pushed onto the stack as a new element
        and returns the self stack."""
        if self.check_empty:
            self.top = OnStack(value)
            return self
        self.top = self.top.push(value)
        return self

    def load(self, *values):
        """This method pushes all elements onto the stack at once
        and returns the stack self."""
        for value in values:
            self.push(value)
        return self

    def pop(self):
        """Returns the value of the top element and updates 'self.top'."""
        if self.check_empty:
            raise ValueError("Cannot pop from empty stack!")
            return None
        value, self.top = self.top.data, self.top.lower
        return value


if __name__ == '__main__':
    a_stack = Stack().load(1, 3, 5, 7)
    print(a_stack.pop(), a_stack.pop(), a_stack.pop(), a_stack.pop())
    a_stack.push(90)
    print(a_stack.pop(), a_stack.pop())
    
