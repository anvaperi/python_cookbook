class FibonacciIterator:
  def __init__(self, stop=10):
    self._stop = stop
    self._current = 0
    self._next = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self._stop <= 0:
      raise StopIteration
    self._stop -= 1
    fib_number = self._current
    self._current, self._next = (
      self._next,
      self._current + self._next,
    )
    return fib_number

if __name__ == '__main__':
  for fib_number in FibonacciIterator():
    print(fib_number, end=' ')