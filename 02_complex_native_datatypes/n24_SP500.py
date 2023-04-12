# # Analyzing the S&P500
# # In this example, you will get your first taste of using itertools to manipulate a large dataset—in particular,
# # the historical daily price data of the S&P500 index.
# #
# # Read data from the CSV file and transform it into a sequence gains of daily percent changes using the “Adj Close” column.
# # Find the maximum and minimum values of the gains sequence, and the date on which they occur.
# # (Note that it is possible that these values are attained on more than on date;
# # in that case, the most recent date will suffice.)
# # Transform gains into a sequence growth_streaks of tuples of consecutive positive values in gains.
# # Then determine the length of the longest tuple in growth_streaks and the beginning and ending dates of the streak.
# # (It is possible that the maximum length is attained by more than one tuple in growth_streaks;
# # in that case, the tuple with the most recent beginning and ending dates will suffice.)
# # The percent change between two values x and y is given by the following formula: (x/y-1)*100
#
# from collections import namedtuple
#
# class DataPoint(namedtuple('DataPoint', ['date', 'value'])):
# 	__slots__ = ()
# 	def __le__(self, other): return self.value <= other.value
# 	def __lt__(self, other): return self.value < other.value
# 	def __gt__(self, other): return self.value > other.value
#
# import csv
#
# from datetime import datetime
#
# def read_prices(csvfile, _strptime=datetime.strptime):
# 	with open(csvfile) as infile:
# 		reader = csv.DictReader(infile)
# 		for row in reader:
# 			yield DataPoint(
# 				date=_strptime(row['Date'], "%d/%m/%Y").date(),
# 				value=float(row['Adj Close'])
# 			)
#
# prices = tuple(read_prices('n24_SP500.csv'))
#
# gains = tuple(
# 	DataPoint(day.date, 100*(day.value/prev_day.value - 1.))
# 	for day, prev_day in zip(prices[1:], prices)
# )
#
# import functools as ft
#
# # max_gain = ft.reduce(max, gains) #XXX lese weiter ↓
# # print(max_gain)
# #
# # # The above solution works, but it isn’t equivalent to the for loop you had before. Do you see why?
# # # Suppose the data in your CSV file recorded a loss every single day. What would the value of max_gain be?
# # #
# # # In the for loop, you first set max_gain = DataPoint(None, 0), so if there are no gains,
# # # the final max_gain value will be this empty DataPoint object. However, the reduce() solution returns the smallest loss.
# # # That is not what you want and could introduce a difficult to find bug.
# import itertools as it
# # only_positives = it.filterfalse(lambda x: x <= 0, [0, 1, -1, 2, -2])
# # print(list(only_positives)) #[1, 2]
# dp0 = DataPoint(None, 0)
# max_gain = ft.reduce( max, it.filterfalse(lambda p: p.value <= 0, gains), dp0 )
# max_loss = ft.reduce( min, it.filterfalse(lambda p: p.value > 0, gains), dp0 )
#
# print(f'{max_loss=}, {max_gain=}')
#
#
# import itertools as it
#
# def consecutive_positives(sequence, zero=0):
# 	def consecutives_generator():
# 		for itr in it.repeat(iter(sequence)):
# 			yield tuple(
# 				it.takewhile(
# 					lambda p: p > zero,
# 					it.dropwhile(lambda p: p <= zero, itr)
# 				)
# 			)
# 	return it.takewhile(lambda t: len(t), consecutives_generator())
#
# print(list(consecutive_positives([0, -1, 2, -3, 4, -5, 7, 6])))
#
# growth_streaks = consecutive_positives(gains, zero=DataPoint(None, 0))
# longest_streak = ft.reduce(
# 	lambda x, y: x if len(x) > len(y) else y, growth_streaks
# )



from collections import namedtuple
import csv
from datetime import datetime
import itertools as it
import functools as ft

class DataPoint(namedtuple('DataPoint', ['date', 'value'])):
	__slots__ = ()
	def __le__(self, other): return self.value <= other.value
	def __lt__(self, other): return self.value < other.value
	def __gt__(self, other): return self.value > other.value

def consecutive_positives(sequence, zero=0):
	def _consecutives():
		for itr in it.repeat(iter(sequence)):
			yield tuple(it.takewhile(
				lambda p: p > zero,
				it.dropwhile(lambda p: p <= zero, itr)
			))
	return it.takewhile(lambda t: len(t), _consecutives())

def read_prices(csvfile, _strptime=datetime.strptime):
	with open(csvfile) as infile:
		reader = csv.DictReader(infile)
		for row in reader:
			yield DataPoint(
				date=_strptime(row['Date'], "%d/%m/%Y").date(),
				value=float(row['Adj Close'])
			)


# Read prices and calculate daily percent change.
prices = tuple(read_prices('n24_SP500.csv'))
gains = tuple(
	DataPoint(day.date, 100*(day.value/prev_day.value - 1.))
	for day, prev_day in zip(prices[1:], prices)
)

# Find maximum daily gain/loss.
zdp = DataPoint(None, 0)  # zero DataPoint
max_gain = ft.reduce(max, it.filterfalse(lambda p: p <= zdp, gains))
max_loss = ft.reduce(min, it.filterfalse(lambda p: p > zdp, gains), zdp)


# Find longest growth streak.
growth_streaks = consecutive_positives(gains, zero=DataPoint(None, 0))
longest_streak = ft.reduce(
	lambda x, y: x if len(x) > len(y) else y, growth_streaks
)

# Display results.
print('Max gain: {1:.2f}% on {0}'.format(*max_gain))
print('Max loss: {1:.2f}% on {0}'.format(*max_loss))

print('Longest growth streak: {num_days} days ({first} to {last})'.format(
	num_days=len(longest_streak),
	first=longest_streak[0].date,
	last=longest_streak[-1].date
))


