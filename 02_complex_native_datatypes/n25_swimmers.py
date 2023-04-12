# from collections import namedtuple
#
# class Event(namedtuple('Event', ['stroke', 'name', 'time'])):
# 	__slots__ = ()
# 	def __lt__(self, other): return self.time < other.time
#
# import csv
# import datetime
# import statistics
#
# def read_events(csvfile, _strptime=datetime.datetime.strptime):
# 	def _median(times):
# 		return statistics.median(
# 			(_strptime(time, '%M:%S:%f').time() for time in row['Times'])
# 		)
# 	fieldnames = ['Event', 'Name', 'Stroke']
# 	with open(csvfile) as infile:
# 		reader = csv.DictReader(infile, fieldnames=fieldnames, restkey='Times')
# 		next(reader)  # skip header
# 		for row in reader:
# 			yield Event(row['Stroke'], row['Name'], _median(row['Times']))
#
# events = tuple(read_events('n25_swimmers.csv'))
#
# for event in events[:5]:
# 	print(event)
#
# # Group the events by stroke.
# # For each stroke:
# # Group its events by swimmer name and determine the best time for each swimmer.
# # Order the swimmers by best time.
# # The first four swimmers make the “A” team for the stroke, and the next four swimmers make the “B” team.
#
# import itertools as it
#
# data = [
# 	{'name': 'Alan', 'age': 34},
# 	{'name': 'Catherine', 'age': 34},
# 	{'name': 'Betsy', 'age': 29},
# 	{'name': 'David', 'age': 33}
# ]
#
# grouped_data = it.groupby(data, key=lambda x: x['age'])
# for key, grp in grouped_data:
# 	print('{}: {}'.format(key, list(grp)))
#
# for key, grp in it.groupby([1, 1, 2, 2, 2, 3]):
# 	print('{}: {}'.format(key, list(grp)))
#
# # When working with groupby(), you need to sort your data on the same key that you would like to group by.
# # Otherwise, you may get unexpected results.
# # This is so common that it helps to write a utility function to take care of this for you:
#
# def sort_and_group(iterable, key=None):
# 	"""Group sorted `iterable` on `key`."""
# 	return it.groupby(sorted(iterable, key=key), key=key)
#
# for stroke, evts in sort_and_group(events, key=lambda evt: evt.stroke):
# 	events_by_name = sort_and_group(evts, key=lambda evt: evt.name)
# 	best_times = (min(evt) for _, evt in events_by_name)
#
# # print('Test')
# # print([(min(i), i, _) for _, i in [[iter([1]), iter([2])], [iter([3]), iter([4])], [iter([5]), iter([6])]]])
# #
# # my_iterable = [1, 2, 3, 4]
# # sm = lambda m, p, list: (p + m * x for x in list)
# # my_hyperiterable = [sm(1, 2, my_iterable), sm(2, 4, my_iterable), sm(10, 5, my_iterable), sm(-1, 0, my_iterable)]
# # my_iterators = [iter(my_hyperiterable)] * 2
# # print([sum(i) for _, i in zip(*(my_iterators))])
# #

from collections import namedtuple
import csv
import datetime
import itertools as it
import statistics


# Define a named tuple to represent a swim event.
class Event(namedtuple('Event', ['stroke', 'name', 'time'])):
	__slots__ = ()

	def __lt__(self, other):
		return self.time < other.time


# Sort and group an iterable using a given key function.
def sort_and_group(iterable, key=None):
	return it.groupby(sorted(iterable, key=key), key=key)


# Group an iterable into fixed-length chunks using zip_longest.
def grouper(iterable, n, fillvalue=None):
	iters = [iter(iterable)] * n
	return it.zip_longest(*iters, fillvalue=fillvalue)


# Read swim events from a CSV file and return an iterator over them.
def read_events(csvfile, _strptime=datetime.datetime.strptime):
	# Define a helper function to compute the median time for a swim event.
	def _median(times):
		return statistics.median(
			(_strptime(time, '%M:%S:%f').time() for time in row['Times'])
		)

	# Read events from the CSV file row by row, skipping the header.
	fieldnames = ['Event', 'Name', 'Stroke']
	with open(csvfile) as infile:
		reader = csv.DictReader(infile, fieldnames=fieldnames, restkey='Times')
		next(reader)  # Skip header.
		for row in reader:
			yield Event(row['Stroke'], row['Name'], _median(row['Times']))


# Load all swim events from the CSV file.
events = tuple(read_events('n25_swimmers.csv'))

# Group swim events by stroke, then by name, and compute the best times for each swimmer.
for stroke, evts in sort_and_group(events, key=lambda evt: evt.stroke):
	events_by_name = sort_and_group(evts, key=lambda evt: evt.name)
	best_times = (min(evt) for _, evt in events_by_name)

	# Sort the best times and group them into teams of 4 swimmers each.
	sorted_by_time = sorted(best_times, key=lambda evt: evt.time)
	teams = zip(('A', 'B'), it.islice(grouper(sorted_by_time, 4), 2))

	# Print the team rosters for each stroke.
	for team, swimmers in teams:
		print('{stroke} {team}: {names}'.format(
			stroke=stroke.capitalize(),
			team=team,
			names=', '.join(swimmer.name for swimmer in swimmers)
		))