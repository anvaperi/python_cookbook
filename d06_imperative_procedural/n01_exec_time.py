import time

def timer(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		print(f"Execution time: {end_time - start_time} seconds")
		return result
	return wrapper

@timer
def some_function():
	a = 'a'
	i = 0
	while i < 6:
		i += 1													# 8 											9 											10 										 11
		a += a + a + a + a + a + a 			# 0.0050890445709228516 s 0.03159666061401367   s 0.21342849731445312  s 1.5498385429382324  s
		a = ''.join([a, a, a, a, a, a]) # 0.0015974044799804688 s 0.0019996166229248047 s 0.018820762634277344 s 0.07212591171264648 s
		# 1.775130271911621 seconds
	print(len(a))
	# do something here
	pass

some_function()