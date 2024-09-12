import pygame, sys
pygame.init()
from ball import Ball
WIDTH = 400
HEIGHT = 500

class Simulation:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ball Dropper")
        self.clock = pygame.time.Clock()
        self.balls = []
        self.balls.append(Ball(pos=[WIDTH/2 + 30, HEIGHT/4], radius=20, color="red", V0=0, elasticity=1, showOverlay=True))
        self.balls.append(Ball([WIDTH/4 - 30, HEIGHT/4], 40, "blue", 100, 0.50, showOverlay=True))
        # # self.ball2 = Ball([WIDTH/4, HEIGHT], 40, "blue", V0=-1000, elasticity=0.5, ball_count=2)
        # self.balls.append(Ball([WIDTH/2 + WIDTH/4, HEIGHT/4], 10, "green", V0=125,elasticity=0.75, showOverlay=True))
        # self.balls.append(Ball([WIDTH/4 + 60, HEIGHT/4], 30, "purple", V0=175, elasticity=0.75, showOverlay=True))
        # self.ball2 = Ball([WIDTH/4, HEIGHT - 20], 20, "blue", -1000, 0.75, 2)
        
    def run(self):
        while True:
            dt = self.clock.tick(60)/1000
            # print(dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            self.display.fill("black")
            for ball in self.balls:
                ball.update(dt)
            # self.ball.update(dt)
            # self.ball2.update(dt)
            # self.ball3.update(dt)
            # self.ball4.update(dt)
  
            pygame.display.update()

if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()

# has_enough_units, has_met_requirements = True