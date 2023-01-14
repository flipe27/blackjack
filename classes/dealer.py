from settings import *

class Dealer:
    def __init__(self, game):
        self.game = game
        self.cards = []
        self.values = 0
        self.alternativeValue = 0
        self.x = SCREEN_WIDTH / 2
        self.y = CARD_BACK_IMAGE.get_height() / 2
        self.isBurst = False
        self.haveRoyal = False
        self.haveShuffle = False

    def dealBeginCards(self):
        for cont in range(0, 2):
            self.receiveCard()
            for player in self.game.players:
                player.receiveCard()

    def receiveCard(self):
        if len(self.game.deck.newDeck) > 0 and not self.isBurst:
            if len(self.cards) == 1:
                self.game.deck.newDeck[0].isShuffle = True
                self.game.deck.newDeck[0].shuffleCard()
                self.haveShuffle = True
            if len(self.cards) == 2 and self.haveShuffle:
                self.cards[1].isShuffle = False
                self.cards[1].shuffleCard()
                self.haveShuffle = False
            else:
                self.cards.append(self.game.deck.newDeck[0])
                self.game.deck.cardsAmount -= 1
                del self.game.deck.newDeck[0]

            self.values = 0
            self.alternativeValue = 0
            for card in self.cards:
                if card.value == 1:
                    self.alternativeValue += 11
                else:
                    self.alternativeValue += card.value
                self.values += card.value

            if self.values > 21:
                self.isBurst = True
            if self.alternativeValue > 21:
                self.alternativeValue = self.values

        for card in self.cards:
            if card.isRoyal:
                self.haveRoyal = True

    def update(self):
        cardsWidth = (len(self.cards) + 1) * CARD_BACK_IMAGE.get_width() / 2

        for i, card in enumerate(self.cards):
            if self.values > 0:
                text = f'{self.values}' if self.values == self.alternativeValue else f'{self.values} / {self.alternativeValue}'

                if self.values == 11 and self.alternativeValue == 21 and self.haveRoyal:
                    text = 'BJ'

                color = (255, 255, 255) if not self.isBurst else (255, 0, 0)
                cardsValuesText = GAME_FONT.render(text, True, color)
                self.game.screen.blit(cardsValuesText, (SCREEN_WIDTH / 2 - cardsValuesText.get_width() / 2, CARD_BACK_IMAGE.get_height() + CARD_BACK_IMAGE.get_height() / 2))

            self.game.screen.blit(card.image, (self.x - cardsWidth + CARD_BACK_IMAGE.get_width() * i + CARD_BACK_IMAGE.get_width() / 2, self.y))
