
class SingleLinkedListElement:
    """This class implements the nodes of the composite 'SingleLinkedList'
    """
    def __init__(self, value, next_one=None):
        """Two attributes: 'data' and 'next_one'."""
        self.data = value
        self.next_one = next_one

    def add(self, value):
        """Returns a new created following item."""
        self.next_one = SingleLinkedListElement(value)
        return self.next_one

    def insert(self, value):
        """Returns a new created preceding item."""
        return SingleLinkedListElement(value, self)

    def __str__(self):
        """The display function only considers the attribute 'data'."""
        return str(self.data)
    
class SingleLinkedList:
    """This is a composite class of 'SingleLinkedListElement'."""
    def __init__(self):
        """One attribute 'head' pointing to the beggining."""
        self.head = None

    def load(self, *values):
        """Adds a list of values to a 'SingleLinkedList' object and
        returns the last element added.
        """
        values_iterator = iter(values)
        if self.head is None:
            self.head = SingleLinkedListElement(next(values_iterator))
        element = self.head
        for value in values_iterator:
            element = element.add(value)
        return element

    def traverse(self):
        """Generator function that yields all values."""
        element = self.head
        while element is not None:
            yield element
            element = element.next_one
        return None
    
    def __str__(self):
        """Returns a space separated string of elements."""
        out = ''
        for element in self.traverse():
            out += str(element) + ' '
        return out

    def insert(self, value):
        """Invokes the 'insert' method of component class."""
        self.head = self.head.insert(value)

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
        if value is None or value == self.head.data:
            value = self.head.data
            self.head = self.head.next_one
            return value
        previous = self.head
        for element in self.traverse():
            if value == element.data:
                previous.next_one = element.next_one
                return value
            previous = element
        return None

            
    
if __name__ == '__main__':
    my_list = SingleLinkedList()
    my_list.load(1,3,5,7,9)
    my_list.delete()
    my_list.insert(30)
    my_list.delete(7)
    print(my_list, my_list.search(5))
