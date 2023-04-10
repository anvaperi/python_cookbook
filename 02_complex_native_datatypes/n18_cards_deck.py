from constant_colors import RED, RESET, code_str
import itertools as it
import random

red = code_str(RED)
reset = code_str(RESET)

print('------WAY VIA CARTESIAN PRODUCT:------')

def format_card(card):
	card_str = card['rank']+card['suit']
	if card['suit'] == '♥' or card['suit'] == '♦':
		card_str = card_str.join([red, reset])
	return card_str

def print_deck(deck, index=0):
	for card in deck:
		if not index % 13:
			print()
		index+=1
		print(format_card(card), end=' ')

def get_shuffled_iterator(deck):
	"""Return iterator over shuffled deck."""
	deck = list(deck) + [joker]
	random.shuffle(deck)
	return deck #XXX iter(list(deck))

def get_cut_iterator(deck, n):
	"""Return an iterator over a deck of cards cut at index `n`."""
	deck = list(deck)
	n += int(len(deck)*random.random())
	n %= len(deck)
	#XXX print(f"{n=}")
	return iter(deck[n:] + deck[:n])


joker = {'rank': '-', 'suit': '𝓙'} # 🃏
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
suits = ['♥', '♦', '♣', '♠']

# cards = ((rank, suit) for suit in suits for rank in ranks)
get_cards_iterator = lambda suits, ranks: ( {'rank': rank, 'suit': suit} for suit, rank in it.product(suits, ranks))
print_deck(get_cards_iterator(suits, ranks))
print()
print_deck(get_shuffled_iterator(get_cards_iterator(suits, ranks)))
print()
print_deck(get_cut_iterator(get_shuffled_iterator(get_cards_iterator(suits, ranks)), -26))  # Cut the deck in half.