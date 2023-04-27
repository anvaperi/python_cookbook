
class DoubleLinkedListElement:
    """This class implements the nodes of the composite 'DoubleLinkedList'
    """
    def __init__(self, value, next_one=None, previous=None):
        """Two attributes: 'data' and 'next_one'."""
        self.data = value
        self.next_one = next_one
        self.previous = previous

    def add(self, value):
        """Returns a new created following item."""
        self.next_one = DoubleLinkedListElement(value, None, self)
        return self.next_one

    def insert(self, value):
        """Returns a new created preceding item."""
        self.previous = DoubleLinkedListElement(value, self)
        return self.previous
        
    def __str__(self):
        """The display function only considers the attribute 'data'."""
        return str(self.data)
    
    
class DoubleLinkedList:
    """This is a composite class of 'DoubleLinkedListElement'."""
    def __init__(self):
        """Attributes 'head' and 'tail' are pointing to the first and
        last elements and attribute 'backwards' becomes true to
        traverse the list in reversed order."""
        self.head = None
        self.tail = None
        self.backwards = False

    def reverse(self):
        self.backwards = not self.backwards

    def load(self, *values):
        """Adds a list of values to a 'SingleLinkedList' object and
        returns the last element added.
        """
        values_iterator = iter(values)
        if self.head is None:
            self.head = DoubleLinkedListElement(next(values_iterator))
        element = self.head
        for value in values_iterator:
            element = element.add(value)
        self.tail = element
        return True

    def traverse(self):
        """Generator function that yields all values."""
        element = self.tail if self.backwards else self.head
        while element is not None:
            yield element
            element = element.previous if self.backwards else element.next_one
        return None
    
    def __str__(self):
        """Returns a space separated string of elements."""
        out = []
        for element in self.traverse():
            out += [str(element)]
        return ' <-> '.join(out)

    def insert(self, value, *, after=None):
        """Invokes the 'insert' method of component class."""
        if after is None and self.backwards:
            self.tail = self.tail.add(value)
        elif after is None:
            self.head = self.head.insert(value)
        else:
            for element in self.traverse():
                if after == element.data:
                    newElement = DoubleLinkedListElement(
                        value, element.next_one, element)
                    element.next_one.previous = newElement
                    element.next_one = newElement

    def search(self, value):
        """Returns the matching index of first occurrence or -1 if not found.
        """
        position = 0
        for element in self.traverse():
            if value == element.data:
                return position
            position += 1 
        return -1

    def delete(self, value=None):
        """Deletes the specified key first match and returns
        the corresponding value or 'None' when not found."""
        if self.head is None:
            raise ValueError("Cannot delete from an empty list!")
            return None
        if self.backwards and (value is None or value == self.tail.data):
            value, self.tail = self.tail.data, self.tail.previous
            return value
        elif not self.backwards and (value is None or value == self.head.data):
            value, self.head = self.head.data, self.head.next_one
            return value 
        for element in self.traverse():
            if value == element.data:
                element.previous.next_one = element.next_one
                element.next_one.previous = element.previous
                return value
        return None

            
if __name__ == '__main__':
    my_list = DoubleLinkedList()
    my_list.load(2, 4, 8, 6, 0)
    print(my_list)
    my_list.delete()
    print(my_list)
    my_list.insert(30)
    print(my_list)
    my_list.delete(6)
    print(my_list)
    my_list.reverse()
    print(my_list, my_list.search(8))
