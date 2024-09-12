import pygame, math
pygame.init()

class OverLay:
    def __init__(self, pos, color, fontSize, values1, values2, radius, V0):
        self.display = pygame.display.get_surface()
        self.pos = pos
        self.color = color
        self.fontSize = fontSize
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)

        self.values1 = values1
        self.values2 = values2

        self.radius = radius

        self.V0 = V0


    def draw(self, pos, values1, values2, value3):
        self.values1 = values1
        self.values2 = values2
        self.pos = pos

        self.text = self.font.render(f"V0: {self.V0}", True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (self.pos[0] + self.radius, self.pos[1] - 25)
        self.display.blit(self.text, self.textRect)

        self.text = self.font.render(f"E: {value3}", True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (self.pos[0] + self.radius, self.pos[1] - 15)
        self.display.blit(self.text, self.textRect)

        self.text = self.font.render(f"{self.values1[0]}: {math.floor(self.values1[1])}", True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (self.pos[0] + self.radius, self.pos[1] - 5)
        self.display.blit(self.text, self.textRect)

        self.text = self.font.render(f"{self.values2[0]}: {math.floor(self.values2[1])}", True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (self.pos[0] + self.radius, self.pos[1] + 5)
        self.display.blit(self.text, self.textRect)

