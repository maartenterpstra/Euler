import itertools
class Card:

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def __lt__(self, other):
		if isinstance(other, Card):
			return self.rank < other.rank
		return NotImplemented

class Hand:
	def __init__(self, cards):
		self.cards = cards
		
	def getCards(self):
		return self.cards

	def getCard(self, index):
		return self.cards[index]

	def setCard(self, index, card):
		self.cards[index] = card

	def addCard(self, card):
		self.cards.append(card)

	def getNthHighest(self, n):
		return self.cards[4 - n].rank

	def getPair(self):
		try:
			return next((x, y) for x, y in itertools.combinations(self.cards, 2) if x.rank ==  y.rank and x != y)
		except:
			return None

	def getTwoPairs(self):
		try:
			return next(((x, y), (a, b)) for x, y, a, b in itertools.combinations(self.cards, 4) if ((x.rank ==  y.rank and x != y) and (a.rank == b.rank and a != b)) and x != a and x != b)
		except:
			return None

	def getThreeOfAKind(self):
		try:
			return next((x, y, z) for x, y, z in zip(self.cards, self.cards[1:], self.cards[2:]) if x.rank == y.rank == z.rank)
		except:
			return None

	def getStraight(self):
		temp = [x for (x, y) in zip(self.cards, self.cards[1:]) if x.rank + 1 == y.rank]
		temp.append(self.cards[4])
		return self.cards if temp == self.cards else None

	def getFlush(self):
		return self.cards if [x for x in self.cards if x.getSuit() == self.cards[0].getSuit()] == self.cards else None

	def getFullHouse(self):
		if self.getThreeOfAKind() == None:
			return None

		# See if there is a pair left if you remove the three of a kind
		remaining = filter(lambda x: x not in self.getThreeOfAKind(), self.cards)
		if remaining[0].rank == remaining[1].rank:
			return self.cards

		return None

	def getFourOfAKind(self):
		foakList = [(w, x, y, z) for w, x, y, z in (zip(self.cards, self.cards[1:], self.cards[2:], self.cards[3:])) if w.rank == x.rank == y.rank == z.rank]
		return foakList if len(foakList) > 0 else None

	def getStraightFlush(self):
		if self.getStraight() and self.getFlush():
			return self.cards

		return None

	def getRoyalFlush(self):
		if self.getStraightFlush() != None and self.cards[0].rank == 10:
			return self.cards

		return None

	def getScore(self):
		if self.getRoyalFlush():
			return (23, 23)
		elif self.getStraightFlush():
			return (22, self.getStraightFlush()[0].rank)
		elif self.getFourOfAKind():
			return (21, self.getFourOfAKind()[0].rank)
		elif self.getFullHouse():
			return (20, self.getThreeOfAKind()[0].rank)
		elif self.getFlush():
			return (19, self.getFlush()[0].rank)
		elif self.getStraight():
			return (18, self.getStraight()[0].rank)
		if self.getThreeOfAKind():
			return (17, self.getThreeOfAKind()[0].rank)
		elif self.getTwoPairs():
			return (16, 0)
		elif self.getPair():
			return (15, self.getPair()[0].rank)
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

	h1 = Hand(sorted(list1))

	tempList1 = hands.split()[5:]
	list2 = []
	for x in tempList1:
		card = Card(getCardScore(x[0]), x[1])
		list2.append(card)

	h2 = Hand(sorted(list2))

	if h1 > h2:
		playerOneWins += 1

print (playerOneWins)