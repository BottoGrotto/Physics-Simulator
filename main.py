import pygame, sys
pygame.init()
from ball import Ball
WIDTH = 400
HEIGHT = 800

class Simulation:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.ball = Ball([WIDTH/2, HEIGHT/4], 10, "red", 100)
        self.ball2 = Ball([WIDTH/4, HEIGHT/4], 20, "blue", 150)

        # font = pygame.font.Font('freesansbold.ttf', 32)
        
    def run(self):
        while True:
            dt = self.clock.tick(60)/1000
            # print(dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            self.display.fill("black")
            self.ball.update(dt)
            self.ball2.update(dt)
            # self.display.blit(self.text, self.textRect)
            pygame.display.update()

if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()

has_enough_units, has_met_requirements = True