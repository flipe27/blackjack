import sys
from settings import *
from classes.deck import Deck
from classes.player import Player
from classes.dealer import Dealer
from classes.options import Options

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Blackjack')
        self.playersAmount = 7
        self.sectorWidth = SCREEN_WIDTH / self.playersAmount
        self.begin = True
        self.mousePressed = False

        self.deck = Deck(self)
        self.players = []
        for cont in range(0, self.playersAmount):
            isPlayer = True if cont == 3 else False
            self.players.append(Player(self, self.sectorWidth * cont + self.sectorWidth / 2 - CARD_BACK_IMAGE.get_width() / 2, isPlayer))
        self.dealer = Dealer(self)
        self.options = Options(self)

    def update(self):
        self.deck.update()
        for player in self.players:
            player.update()
        self.dealer.update()
        self.options.update()

        pygame.display.update()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.dealer.receiveCard()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePressed = True

    def run(self):
        while True:
            self.clock.tick(60)

            self.screen.blit(BACKGROUND_IMAGE, (0, 0))

            if self.begin:
                self.dealer.dealBeginCards()
                self.begin = False

            self.checkEvents()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()
