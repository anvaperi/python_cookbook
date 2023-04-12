generator_expression = (item for item in [1, 2, 3, 4])
for item in generator_expression:
  print(item)

print('--Generators--')

# generator
def to_square_g(numbers, f):
  for number in numbers:
    if number > 20 or number < 10:
      yield f(number)
# generator expression
to_square_gexpr = lambda numbers, f: ( f(number) for number in numbers if number > 20 or number < 10 )

for square in     to_square_g([1, 2, 3, 4, 5], lambda t: t ** 2): print(square)
print('---')
for square in to_square_gexpr([1, 2, 3, 4, 5], lambda t: t ** 2): print(square)
print('---')
# import math_pipeline as mpl # deprecated
# list(mpl.to_string(mpl.to_square(mpl.to_even(range(20)))))

my_pipeline = lambda raw_data, f: (f(i) for i in raw_data if not i % 2)
for element in my_pipeline(range(20), lambda t: t ** 2): print(element)