# asynchronous iterators implement the asynchronous iterator protocol, which consists of two methods:
# .__aiter__() returns an asynchronous iterator, typically self.
# .__anext__() must return an awaitable object from a stream. It must raise a StopAsyncIteration

import asyncio
from random import randint

class AsyncIterable:
	def __init__(self, stop):
		self._stop = stop
		self._index = 0

	def __aiter__(self):
		return self

	async def __anext__(self):
		if self._index >= self._stop:
			raise StopAsyncIteration
		await asyncio.sleep(value := randint(1, 3))
		self._index += 1
		return value