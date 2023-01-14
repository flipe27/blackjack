from settings import *
from classes.card import Card
import random

class Deck:
    def __init__(self, game):
        self.game = game
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.allCards = []
        self.addCards()
        self.newDeck = []
        self.shuffle()
        self.cardsAmount = len(self.newDeck)
        self.cardsBackImage = pygame.transform.rotate(CARD_BACK_IMAGE, 270)

    def shuffle(self):
        while len(self.allCards) > 0:
            chosenCard = random.choice(self.allCards)
            self.newDeck.append(chosenCard)
            self.allCards.remove(chosenCard)

    def addCards(self):
        for suit in self.suits:
            for cont in range(2, 15):
                self.allCards.append(Card(suit, cont))

    def update(self):
        cardsAmountText = GAME_FONT.render(f'{self.cardsAmount}', True, (255, 255, 255))

        self.game.screen.blit(self.cardsBackImage, (SCREEN_WIDTH - self.cardsBackImage.get_width(), 0))
        self.game.screen.blit(cardsAmountText, (SCREEN_WIDTH - self.cardsBackImage.get_width() / 2 - cardsAmountText.get_width() / 2, self.cardsBackImage.get_height() - 10))
