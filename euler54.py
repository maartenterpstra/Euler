import itertools
class Card:

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def __eq__(self, other):
		if isinstance(other, Card):
			return self.rank == other.rank and self.suit == other.suit
		return NotImplemented

	def __lt__(self, other):
		if isinstance(other, Card):
			return self.rank < other.rank
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Card):
			return not self.__eq__(other) and not self.__lt__(other)
		return NotImplemented

	def __ne__(self, other):
		if isinstance(other, Card):
			return not self.__eq__(other)
		return NotImplemented

	def __ge__(self, other):
		if isinstance(other, Card):
			return self.__eq__(other) or self.__gt__(other)
		return NotImplemented

	def __le__(self, other):
		if isinstance(other, Card):
			return self.__eq__(other) or self.__lt__(other)

		return NotImplemented

	def __str__(self):
		return "({0}, {1})".format(self.rank, self.suit)

	def __repr__(self):
		return self.__str__()

class Hand:
	def __init__(self, cards):
		self.cards = cards

	def __repr__(self):
		return self.cards.__str__()

	def __str__(self):
		return self.__repr__()

	def getCards(self):
		return self.cards

	def getCard(self, index):
		return self.cards[index]

	def setCard(self, index, card):
		self.cards[index] = card

	def addCard(self, card):
		self.cards.append(card)

	def getNthHighest(self, n):
		cardList = sorted(self.cards, key=lambda x: x.rank, reverse=True)
		return cardList[n].rank

	def getPair(self):
		cardList = sorted(self.cards)
		try:
			return next((x, y) for x, y in itertools.combinations(cardList, 2) if x.rank ==  y.rank and x != y)
		except:
			return None

	def getTwoPairs(self):
		cardList = sorted(self.cards)
		try:
			return next(((x, y), (a, b)) for x, y, a, b in itertools.combinations(cardList, 4) if ((x.rank ==  y.rank and x != y) and (a.rank == b.rank and a != b)) and x != a and x != b)
		except:
			return None

	def getThreeOfAKind(self):
		ret = None
		cardList = sorted(self.cards)
		combos = zip(cardList, cardList[1:], cardList[2:])
		for (x, y, z) in combos:
			if x.rank == y.rank == z.rank:
				ret = (x, y, z)
				break

		return ret

	def getStraight(self):
		cardList = sorted(self.cards)
		for x in range(1, len(cardList)):
			#print cardList[x].rank
			if cardList[x].rank - 1 != cardList[x-1].rank:
				return None

		return self.cards

	def getFlush(self):
		return self.cards if len([x for x in self.cards if x.getSuit() == self.cards[0].getSuit()]) == len(self.cards) else None

	def getFullHouse(self):
		if self.getThreeOfAKind() == None:
			return None

		# See if there is a pair left if you remove the three of a kind
		remaining = filter(lambda x: x not in self.getThreeOfAKind(), self.cards)
		if remaining[0].rank == remaining[1].rank:
			return self.cards

		return None

	def getFourOfAKind(self):
		cardList = sorted(self.cards)
		foakList = [(w, x, y, z) for w, x, y, z in (zip(cardList, cardList[1:], cardList[2:], cardList[3:])) if w.rank == x.rank == y.rank == z.rank]
		return foakList if len(foakList) > 0 else None

	def getStraightFlush(self):
		if self.getStraight() and self.getFlush():
			return self.cards

		return None

	def getRoyalFlush(self):
		cardList = sorted(self.cards)
		if self.getStraightFlush() != None and cardList[0].rank == 10:
			return self.cards

		return None

	def getScore(self):
		if self.getRoyalFlush():
			return (100, 100)
		elif self.getStraightFlush():
			return (99, self.getStraightFlush()[0].rank)
		elif self.getFourOfAKind():
			return (98, self.getFourOfAKind()[0].rank)
		elif self.getFullHouse():
			return (97, self.getThreeOfAKind()[0].rank)
		elif self.getFlush():
			return (96, self.getFlush()[0].rank)
		elif self.getStraight():
			return (95, self.getStraight()[0].rank)
		if self.getThreeOfAKind():
			return (94, self.getThreeOfAKind()[0].rank)
		elif self.getTwoPairs():
			return (93, 0)
		elif self.getPair():
			return (92, self.getPair()[0].rank)
		else: 
			return self.getNthHighest(0)

	def __gt__(self, other):
		if isinstance(other, Hand):
			thisScore = self.getScore()
			otherScore = other.getScore()
			if thisScore == otherScore:
				i = 0
				while(self.getNthHighest(i) == other.getNthHighest(i)):
					i += 1
				return self.getNthHighest(i) > other.getNthHighest(i)
			else:
				return thisScore > otherScore

		return NotImplemented

def getCardScore(x):
	if x == 'T':
		return 10
	elif x == 'J':
		return 11
	elif x == 'Q':
		return 12
	elif x == 'K':
		return 13
	elif x == 'A':
		return 14
	else:
		return int(x)

playerOneWins = 0
lines = [line.strip() for line in open('poker.txt')]
for hands in lines:
	tempList = hands.split()[:5]
	list1 = []
	for x in tempList:
		card = Card(getCardScore(x[0]), x[1])
		list1.append(card)

	h1 = Hand(list1)

	tempList1 = hands.split()[5:]
	list2 = []
	for x in tempList1:
		card = Card(getCardScore(x[0]), x[1])
		list2.append(card)

	h2 = Hand(list2)

	if h1 > h2:
		playerOneWins += 1

print (playerOneWins)