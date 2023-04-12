from collections import namedtuple

class Event(namedtuple('Event', ['stroke', 'name', 'time'])):
	__slots__ = ()
	def __lt__(self, other): return self.time < other.time

import csv
import datetime
import statistics

def read_events(csvfile, _strptime=datetime.datetime.strptime):
	def _median(times):
		return statistics.median(
			(_strptime(time, '%M:%S:%f').time() for time in row['Times'])
		)
	fieldnames = ['Event', 'Name', 'Stroke']
	with open(csvfile) as infile:
		reader = csv.DictReader(infile, fieldnames=fieldnames, restkey='Times')
		next(reader)  # skip header
		for row in reader:
			yield Event(row['Stroke'], row['Name'], _median(row['Times']))

events = tuple(read_events('n25_swimmers.csv'))

for event in events[:5]:
	print(event)

# Group the events by stroke.
# For each stroke:
# Group its events by swimmer name and determine the best time for each swimmer.
# Order the swimmers by best time.
# The first four swimmers make the “A” team for the stroke, and the next four swimmers make the “B” team.

import itertools as it

data = [
	{'name': 'Alan', 'age': 34},
	{'name': 'Catherine', 'age': 34},
	{'name': 'Betsy', 'age': 29},
	{'name': 'David', 'age': 33}
]

grouped_data = it.groupby(data, key=lambda x: x['age'])
for key, grp in grouped_data:
	print('{}: {}'.format(key, list(grp)))

for key, grp in it.groupby([1, 1, 2, 2, 2, 3]):
	print('{}: {}'.format(key, list(grp)))

# When working with groupby(), you need to sort your data on the same key that you would like to group by.
# Otherwise, you may get unexpected results.
# This is so common that it helps to write a utility function to take care of this for you:

def sort_and_group(iterable, key=None):
	"""Group sorted `iterable` on `key`."""
	return it.groupby(sorted(iterable, key=key), key=key)

