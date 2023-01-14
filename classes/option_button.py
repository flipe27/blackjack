from settings import *

class OptionButton:
    def __init__(self, game, x, y, color, text):
        self.game = game
        self.x = x
        self.y = y
        self.color = color
        self.size = OPTION_BUTTON_SIZE
        self.text = text

    def checkClick(self):
        mousePos = pygame.mouse.get_pos()

        if self.game.mousePressed:
            if self.x <= mousePos[0] <= self.x + self.size and self.y <= mousePos[1] <= self.y + self.size:
                self.game.mousePressed = False

    def draw(self):
        textButton = OPTION_BUTTON_FONT.render(self.text, True, (255, 255, 255))

        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.size, self.size), border_radius=5)
        self.game.screen.blit(textButton, (self.x + self.size / 2 - textButton.get_width() / 2, self.y + self.size / 2 - textButton.get_height() / 2))
