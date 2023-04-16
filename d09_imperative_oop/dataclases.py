from dataclasses import dataclass, make_dataclass, field, fields
from math import asin, cos, radians, sin, sqrt
from typing import List, Any

import sys
sys.path.append('../d02_iterables_and_iterators/')
from constant_colors_emph import RED, RESET, code_str


@dataclass
class InventoryItem:
	"""Class for keeping track of an item in inventory."""
	name: str
	unit_price: float
	quantity_on_hand: int = 0

	def total_cost(self) -> float:
		return self.unit_price * self.quantity_on_hand

#=========================================================================================================

# latitude +-90N/S, Longitude +-180EW

Coordinate = make_dataclass('Coordinate', ['name', 'latitude_sn_deg', 'longitude_we_deg']) # eq to following

@dataclass
class Coordinate:
	name: str
	latitude_sn_deg: float = .0
	longitude_we_deg: float = .0


	def distance_to(self, other):
		earth_radius_km = 6371
		sinsq = lambda z: (sin(radians(z))) ** 2
		cos_deg = lambda z: cos(radians(z))

		radicand = sinsq((other.latitude_sn_deg  - self.latitude_sn_deg)  / 2) + \
							 sinsq((other.longitude_we_deg - self.longitude_we_deg) / 2) * \
				       cos_deg(other.latitude_sn_deg) * cos_deg(self.latitude_sn_deg)

		return 2 * earth_radius_km * asin(sqrt(radicand))

# oslo = Coordinate('Oslo', 59.9, 10.8)
# vancouver = Coordinate('Vancouver', 49.3, -123.1)
# print(f'{oslo.name} is at {oslo.latitude_sn_deg}°N, {oslo.longitude_we_deg}°E')
# print(f'{oslo.distance_to(vancouver)=}')

# The field() specifier is used to customize each field of a data class individually.
# For reference, these are the parameters field() supports:
# -	default: Default value of the field
# -	default_factory: Function that returns the initial value of the field
# -	init: Use field in .__init__() method? (Default is True.)
# -	repr: Use field in repr of the object? (Default is True.)
# -	compare: Include the field in comparisons? (Default is True.)
# -	hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
# -	metadata: A mapping with information about the field

@dataclass
class Position:
	name: str
	lat: float = field(default=0.0, metadata={'unit': 'degrees', 'term': 'latitude'})
	lon: float = field(default=0.0, metadata={'unit': 'degrees', 'term': 'longitude'})


lat_unit = fields(Position)[2].metadata['unit']
for each_field in fields(Position):
	print()
	for each_subfield in ((str(each_field))[6:-1]).replace('=', ':\t').split(','):
		print(each_subfield)

#========================================================================================================

@dataclass
class WithoutExplicitTypes:
	name: Any
	value: Any = 42

#========================================================================================================

# @dataclass() decorator in parentheses. The following parameters are supported:
#  - init: Add .__init__() method? (Default is True.)
#  - repr: Add .__repr__() method? (Default is True.)
#  - eq: Add .__eq__() method? (Default is True.)
#  - order: Add ordering methods? (Default is False.)
#  - unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
#  - frozen: If True, assigning to fields raise an exception. (Default is False.)

SUITS = '𝓙♣♦♥♠'
RANKS = '_-A23456789XJQK'

@dataclass(order=True)
class PlayingCard:
	rank: str
	suit: str

	def __post_init__(self): #XXX no funciona!!
		self.sort_index = (RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit))

	def __str__(self):
		to_str = self.rank + self.suit
		if self.suit == '♥' or self.suit == '♦' or self.rank == '_':
			to_str = to_str.join([code_str(RED), code_str(RESET)])
		return to_str

	# def __repr__(self):
	# 	suit_to_str = self.suit if self.suit == '♣' or self.suit == '♠' else chr(ord(self.suit) - 4)
	# 	return suit_to_str + self.rank


#  In general, a Python object has two different string representations:
#  - repr(obj) is defined by obj.__repr__() and should return a developer-friendly representation of obj.
# 	If possible, this should be a code that can recreate obj. Data classes do this.
#  - str(obj) is defined by obj.__str__() and should return a user-friendly representation of obj.
# 	Data classes do not implement a .__str__() method, so Python will fall back to the .__repr__() method.


def make_french_deck():
	return [PlayingCard(i_rank, i_suit) for i_suit in SUITS[1:] for i_rank in RANKS[2:]] + \
		[PlayingCard(RANKS[1], SUITS[0])] * 2 + [PlayingCard(RANKS[0], SUITS[0])]

@dataclass
class Deck:
	cards: List[PlayingCard] = field(default_factory=make_french_deck)

	def __repr__(self):
		cards = ', '.join(f'{c!s}' for c in self.cards)
		return f'{self.__class__.__name__}({cards})'


for card_index, each_card in enumerate(Deck().cards):
	print('\n' if not card_index % 13 else '', each_card, end=' ')
print('\n')

print(Deck())

for card_index, each_card in enumerate(Deck().cards):
	print('\n' if not card_index % 13 else '', each_card, end=' ')
print('\n')

queen_of_hearts = PlayingCard('Q', '♥')
ace_of_spades = PlayingCard('A', '♠')
joker = PlayingCard('-', '𝓙')
two_cards = Deck([queen_of_hearts, ace_of_spades])

print(ace_of_spades > queen_of_hearts)
#print(joker > queen_of_hearts)
#print(Deck(sorted(make_french_deck())))

l=[i.sort_index for  i in Deck(make_french_deck()).cards]

print(l)
mmm = [1, 6, 2, 4].sort()
print(mmm)

print(['Ford', 'BMW', 'Volvo'].sort())