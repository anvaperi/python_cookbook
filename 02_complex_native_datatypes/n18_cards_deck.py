from constant_colors_emph import RED, RESET, code_str
#from n19_iterator_shuffle import iterator_shuffle
import itertools as it
import random

turn_red = code_str(RED)
reset = code_str(RESET)

print('------WAY VIA CARTESIAN PRODUCT:------')

def format_card(card):
	card_str = card['rank']+card['suit']
	if card['suit'] == '♥' or card['suit'] == '♦':
		card_str = turn_red + card_str + reset
	return card_str

def print_deck(deck, index=0):
	for card in deck:
		if index and not index % 13:
			print()
		index+=1
		print(format_card(card), end=' ')

def shuffle(deck):
	"""Return iterator over shuffled deck."""
	deck = list(deck) + [joker] # !! It uses an iterable on memory!!
	random.shuffle(deck)
	return deck #XXX iter(list(deck))

#XXX FAULTY!!
# def get_shuffled_iterator(deck, to_add_element=None, times=3, pause=int(53*random.random())):
# 	time_counter = 0
# 	if to_add_element is not None and time_counter > 0:
# 		to_add_element=None
# 		pause = 0
# 	while time_counter < times:
# 		deck = iterator_shuffle(deck, pause, to_add_element)
# 	return deck

# worse alternative:
# def get_cut_iterator(deck, n):
# 	"""Return an iterator over a deck of cards cut at index `n`."""
# 	deck = list(deck)
# 	n += int(len(deck)*random.random()) # !! It uses an iterable on memory!!
# 	n %= len(deck)
# 	#XXX print(f"{n=}")
# 	return iter(deck[n:] + deck[:n])

def cut(deck, n):
	"""Return an iterator over a deck of cards cut at index `n`."""
	n %= 53
	deck1, deck2 = it.tee(deck, 2)
	top = it.islice(deck1, n)
	bottom = it.islice(deck2, n, None)
	return it.chain(bottom, top)

def alternate(deck, deck_len=53):
	"""Return an iterator over a deck of cards cut at index `n`."""
	#XXX step = int(5*random.random())
	deck = cut(deck, 26 + int(11*random.random()))
	deck1, deck2 = it.tee(deck, 2)
	left_hand = it.islice(deck1, 0, None, 2)
	right_hand = it.islice(deck2, 1, None, 2)
	return it.chain(left_hand, right_hand)

def deal(deck, hands_count=1, hand_size=5):
	return tuple(  zip(*( it.islice(itr, hands_count) for itr in [iter(deck)] * hand_size ))  )

joker = {'rank': '-', 'suit': '𝓙'} # 🃏
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
suits = ['♥', '♦', '♣', '♠']

# cards = ((rank, suit) for suit in suits for rank in ranks)
get_cards_iterator = lambda suits, ranks: ( {'rank': rank, 'suit': suit} for suit, rank in it.product(suits, ranks))

print('Ordered deck:')
print_deck(get_cards_iterator(suits, ranks))

print('\nThrice alternated deck:')
print_deck(alternate(alternate(alternate(get_cards_iterator(suits, ranks)))))

print('\nShuffled deck:')
# print_deck(get_shuffled_iterator(get_cards_iterator(suits, ranks)))
print_deck(shuffle(get_cards_iterator(suits, ranks)))

print('\nCut deck:')
print_deck(cut(shuffle(get_cards_iterator(suits, ranks)), -26))  # Cut the deck in half.

print('\nHands:')
my_deck = cut(shuffle(get_cards_iterator(suits, ranks)), -26) # iterator
hands = deal( my_deck, hands_count=3)
for each_hand in hands:
	print_deck(each_hand)
	print()

print('\n', len(tuple(my_deck)), ' cards left. ')

print('\nHands:')
hands = deal(get_cards_iterator(suits, ranks), hands_count=3)
for each_hand in hands:
	print_deck(each_hand)
	print()

