
class SingleLinkedListElement:
    """This class implements the nodes of the 
    Circular Single Linked List
    """
    def __init__(self, value, next_one=None):
        """Two attributes: 'data' and 'next_one'."""
        self.data = value
        self.next_one = next_one

    def add(self, value):
        """Returns a new created following item."""
        self.next_one = SingleLinkedListElement(value, self.next_one)
        return self

    def insert(self, value):
        """Returns a new created preceding item."""
        self.data, value = value, self.data
        return self.add(value)

    def __str__(self):
        """The display function only considers the attribute 'data'."""
        return str(self.data)

    
class CircularSingleLinkedListHead(SingleLinkedListElement):
    """This class connects with elements of class
    'CircularSingleLinkedListElement'.
    """
    def __init__(self, value, next_one=None):
        """One attribute 'head' pointing to the beggining."""
        super().__init__(value, next_one)

    def make_circular(self):
        self.next_one = self
        
    def load(self, *values):
        """Adds a list of values to a 'SingleLinkedList' object and
        returns the last element added.
        """
        element = self
        for value in values:
            element = element.add(value).next_one
        element.next_one = self
        return element

    def traverse(self):
        """Generator function that yields all values."""
        yield self
        head_id = id(self)
        element = self.next_one
        while id(element) != head_id:
            #print('yield: ', element)
            yield element
            element = element.next_one
        return None

    def get_last(self):
        head_id = id(self)
        for element in self.traverse():
            if id(element.next_one) == head_id:
                return element
            #print('for: ', element)    
        return None
            
    def __str__(self):
        """Returns a space separated string of elements."""
        out = ''
        for element in self.traverse():
            out += str(element.data) + ' '
        return out

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
        if self.data is None:
            raise ValueError("Cannot delete from an empty list!")
        if value is None or value == self.data:
            value = self.data
            if id(self) == id(self.next_one):
                self.data = None
                return value
            self.data = self.next_one.data
            self.next_one = self.next_one.next_one
            return value
        previous = self
        for element in self.traverse():
            if value == element.data:
                previous.next_one = element.next_one
                return value
            previous = element
        return None


if __name__ == '__main__':
    my_list = CircularSingleLinkedListHead(8)
    my_list.make_circular()
    my_list.load(1,3,5,7,9)
    my_list.delete()
    my_list.insert(4)
    my_list.insert(30)
    my_list.delete(7)
    print('index of 5: ', my_list.search(5))
    print(my_list)
