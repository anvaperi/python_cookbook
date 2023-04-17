from dataclasses import dataclass, make_dataclass, field, fields
from typing import List

import sys
sys.path.append('../d02_iterables_and_iterators/')
from constant_colors_emph import RED, RESET, code_str

# @dataclass() decorator in parentheses. The following parameters are supported:
#  - init: Add .__init__() method? (Default is True.)
#  - repr: Add .__repr__() method? (Default is True.)
#  - eq: Add .__eq__() method? (Default is True.)
#  - order: Add ordering methods? (Default is False.)
#  - unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
#  - frozen: If True, assigning to fields raise an exception. (Default is False.)



	# def __repr__(self):
	# 	suit_to_str = self.suit if self.suit == '♣' or self.suit == '♠' else chr(ord(self.suit) - 4)
	# 	return suit_to_str + self.rank


#  In general, a Python object has two different string representations:
#  - repr(obj) is defined by obj.__repr__() and should return a developer-friendly representation of obj.
# 	If possible, this should be a code that can recreate obj. Data classes do this.
#  - str(obj) is defined by obj.__str__() and should return a user-friendly representation of obj.
# 	Data classes do not implement a .__str__() method, so Python will fall back to the .__repr__() method.


@dataclass(order=True)
class PlayingCard:
	SUITS = '♣♦♥♠' #XXX '𝓙♣♦♥♠'
	RANKS = 'A23456789XJQK' #XXX '_-A23456789XJQK'
	rank: str
	suit: str

	def __post_init__(self): #XXX no funciona!!
		if self.rank not in PlayingCard.RANKS or self.suit not in PlayingCard.SUITS:
			self.sort_index = -1
		else:
			self.sort_index = (PlayingCard.RANKS.index(self.rank) * len(PlayingCard.SUITS) +
												 PlayingCard.SUITS.index(self.suit))

	def __str__(self):
		to_str = self.rank + self.suit
		if self.suit == '♥' or self.suit == '♦' or self.rank == '_':
			to_str = to_str.join([code_str(RED), code_str(RESET)])
		return to_str


@dataclass
class Deck:
	cards: List[PlayingCard] =  field(default_factory= lambda :
		# 2 normal Jokers and a red one
		[PlayingCard('-', '𝓙')] * 2 + [PlayingCard('_', '𝓙')] + \
		# The 52 normal cards
		[PlayingCard(i_rank, i_suit)
		 for i_rank in PlayingCard.RANKS
		 for i_suit in PlayingCard.SUITS]
	)

	# def __post_init__(self):
	# 	sorted_cards = []
	# 	for card in self.cards:
	# 		sorted_cards.append(Data(card))
	# 	Data.__index__(PlayingCard.__post_init__)
	#
	#

	def __repr__(self):
		cards = ', '.join(f'{c!s}' for c in self.cards)
		return f'{self.__class__.__name__}({cards})'


for card_index, each_card in enumerate(Deck().cards):
	print('\n' if not card_index % 13 else '', each_card, end=' ')
print('\n')


queen_of_hearts = PlayingCard('Q', '♥')
ace_of_spades = PlayingCard('A', '♠')
joker = PlayingCard('-', '𝓙')
two_cards = Deck([queen_of_hearts, ace_of_spades])

print(f'{ace_of_spades > queen_of_hearts=}')
print(f'{joker > queen_of_hearts=}')


