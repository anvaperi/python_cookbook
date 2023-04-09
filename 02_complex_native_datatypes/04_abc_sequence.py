from collections.abc import Iterator

class SequenceIterator(Iterator):
  def __init__(self, sequence):
    self.__sequence = sequence
    self.__index = 0

  def __next__(self):
    if self.__index >= len(self.__sequence):
      raise StopIteration
    item = self.__sequence[self.__index]
    self.__index += 1
    return item

if __name__ == '__main__':
	for item in SequenceIterator([1, 2, 3, 4]):
		print(item)
