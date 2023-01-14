from settings import *

class Card:
    def __init__(self, suit, index):
        self.suit = suit
        self.index = index
        self.isShuffle = False
        self.image = pygame.image.load(os.path.join(f'images/{self.suit}', f'{self.index}.png'))
        self.value = self.defineValue()
        self.isRoyal = True if 11 <= self.index <= 13 else False

    def shuffleCard(self):
        if self.isShuffle:
            self.image = CARD_BACK_IMAGE
            self.value = 0
        else:
            self.image = pygame.image.load(os.path.join(f'images/{self.suit}', f'{self.index}.png'))
            self.value = self.defineValue()

    def defineValue(self):
        if self.index < 11:
            return self.index
        elif 11 <= self.index < 14:
            return 10
        else:
            return 1
