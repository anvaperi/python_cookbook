from collections.abc import Iterator

class SequenceIterator(Iterator):
  def __init__(self, sequence):
    self._sequence = sequence
    self._index = 0

  def __next__(self):
    if self._index >= len(self._sequence):
      raise StopIteration
    item = self._sequence[self._index]
    self._index += 1
    return item

if __name__ == '__main__':
  for item in SequenceIterator([1, 2, 3, 4]):
    print(item)
