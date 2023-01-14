from settings import *
from classes.option_button import OptionButton

class Options:
    def __init__(self, game):
        self.game = game
        self.width = SCREEN_WIDTH / 2
        self.height = 80
        self.x = SCREEN_WIDTH / 2 - self.width / 2
        self.y = SCREEN_HEIGHT / 2 - self.height / 2
        self.buttonsList = []
        self.defineButtons()

    def defineButtons(self):
        buttons = ['+', '2x', '/', '--']
        colors = [(0, 200, 0), (200, 200, 0), (200, 0, 0), (0, 0, 200)]

        buttonSectionWidth = self.width / 4
        buttonY = self.y + self.height / 2 - OPTION_BUTTON_SIZE / 2

        for cont in range(len(buttons)):
            buttonX = self.x + buttonSectionWidth * cont + buttonSectionWidth / 2 - OPTION_BUTTON_SIZE / 2
            self.buttonsList.append(OptionButton(self.game, buttonX, buttonY, colors[cont], buttons[cont]))

    def update(self):
        pygame.draw.rect(self.game.screen, (127, 127, 127), (self.x, self.y, self.width, self.height), 3, border_radius=5)
        for button in self.buttonsList:
            button.draw()
            button.checkClick()
