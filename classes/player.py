from settings import *

class Player:
    def __init__(self, game, x, isPlayer):
        self.game = game
        self.cards = []
        self.values = 0
        self.alternativeValue = 0
        self.x = x
        self.y = SCREEN_HEIGHT - 50 - CARD_BACK_IMAGE.get_height()
        self.isPlayer = isPlayer
        self.isBurst = False
        self.haveRoyal = False
        self.alreadyDouble = False
        self.alreadyStop = False
        self.options = self.checkPlayerOptions()
        self.chipsAmount = 0

    def checkPlayerOptions(self):
        canOrder = False
        canDouble = False
        canStop = False
        canSplit = False

        if self.values <= 21:
            canOrder = True
        if not self.alreadyDouble:
            canDouble = True
        if not self.alreadyStop:
            canStop = True
        if len(self.cards) == 2 and self.cards[0].value == self.cards[1].value:
            canSplit = True

        return [canOrder, canDouble, canStop, canSplit]

    def receiveCard(self):
        if len(self.game.deck.newDeck) > 0 and not self.isBurst:
            self.cards.append(self.game.deck.newDeck[0])
            self.game.deck.cardsAmount -= 1

            self.values = 0
            self.alternativeValue = 0
            for card in self.cards:
                if card.value == 1:
                    self.alternativeValue += 11
                else:
                    self.alternativeValue += card.value
                self.values += card.value

            del self.game.deck.newDeck[0]

            if self.values > 21:
                self.isBurst = True
            if self.alternativeValue > 21:
                self.alternativeValue = self.values

        for card in self.cards:
            if card.isRoyal:
                self.haveRoyal = True

    def update(self):
        self.options = self.checkPlayerOptions()

        for i, card in enumerate(self.cards):
            text = f'{self.values}' if self.values == self.alternativeValue else f'{self.values} / {self.alternativeValue}'

            if self.values == 11 and self.alternativeValue == 21 and self.haveRoyal:
                text = 'BJ'

            color = (255, 255, 0) if self.isPlayer else (255, 255, 255)
            cardsValuesText = GAME_FONT.render(text, True, color)

            if self.isBurst:
                cardsValuesText = GAME_FONT.render(text, True, (255, 0, 0))

            self.game.screen.blit(card.image, (self.x, self.y - i * CARD_BACK_IMAGE.get_height() / 3))
            self.game.screen.blit(cardsValuesText, (self.x + CARD_BACK_IMAGE.get_width() / 2 - cardsValuesText.get_width() / 2, self.y + CARD_BACK_IMAGE.get_height()))
