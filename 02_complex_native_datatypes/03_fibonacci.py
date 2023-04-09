class FibonacciIterator:
  def __init__(self, stop=10):
    self.__stop = stop
    self.__current = 0
    self.__next = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.__stop <= 0:
      raise StopIteration
    self.__stop -= 1
    fib_number = self.__current
    self.__current, self.__next = (
      self.__next,
      self.__current + self.__next,
    )
    return fib_number

if __name__ == '__main__':
  for fib_number in FibonacciIterator():
    print(fib_number, end=' ')