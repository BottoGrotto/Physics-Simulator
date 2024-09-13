import pygame, sys
pygame.init()
from ball import Ball
from mouseDragEffect import DragEffect
from dataOverlay import SingleOverlay
WIDTH = 400
HEIGHT = 600

class Simulation:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ball Dropper")
        self.clock = pygame.time.Clock()
        self.balls = []
        # self.balls.append(Ball(pos=[WIDTH/2 + 30, HEIGHT/4], radius=20, color="white", V0=0, elasticity=1, showOverlay=True))
        self.balls.append(Ball([WIDTH/4 - 30, HEIGHT/4], 40, "white", 500, 0.25, showOverlay=True))
        self.dragging = False
        self.mouse_move_amount = (0, 0)
        # # self.ball2 = Ball([WIDTH/4, HEIGHT], 40, "blue", V0=-1000, elasticity=0.5, ball_count=2)
        # self.balls.append(Ball([WIDTH/2 + WIDTH/4, HEIGHT/4], 10, "green", V0=125,elasticity=0.75, showOverlay=True))
        # self.balls.append(Ball([WIDTH/4 + 60, HEIGHT/4], 30, "purple", V0=175, elasticity=0.75, showOverlay=True))
        # self.ball2 = Ball([WIDTH/4, HEIGHT - 20], 20, "blue", -1000, 0.75, 2)
        # pygame.mouse.set_visible(False)
        self.mouseDragList = []
        self.pressed = False
        self.allOverlaysOff = False

        self.ballToMakeRadius = 10
        self.ballToMakeElasticity = 0.75

        self.dragOverlay = SingleOverlay(pygame.mouse.get_pos(), "white", 10, ("V", 0), 5)
        
    def run(self):
        while True:
            mousePos = pygame.mouse.get_pos()
            dt = self.clock.tick(60)/1000
            # print(dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if event.type == pygame.MOUSEBUTTONDOWN and event.type != pygame.MOUSEWHEEL:
                #     pygame.mouse.get_rel()
                #     # self.dragEffect = DragEffect(5, "white", 2, pygame.mouse.get_pos())
                #     self.dragging = True
                #     print('Mouse button pressed!')
                # if event.type == pygame.MOUSEBUTTONUP:
                #     self.mouse_move_amount = pygame.mouse.get_rel()
                #     # self.dragEffect = None
                #     self.dragging = False

                if event.type == pygame.MOUSEWHEEL:
                    # print(event)
                    if self.ballToMakeRadius > 5 or (self.ballToMakeRadius == 5 and event.y > 0):
                        self.ballToMakeRadius += event.y

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        # print("Hello")
                        self.balls = []
                    if event.key == pygame.K_o:
                        if self.allOverlaysOff == False:
                            for ball in self.balls:
                                ball.showOverlay = False
                            self.allOverlaysOff = True
                        else:
                            for ball in self.balls:
                                ball.showOverlay = True
                            self.allOverlaysOff = False

                    if event.key == pygame.K_UP:
                        
                        self.ballToMakeRadius += 1
                    elif event.key == pygame.K_DOWN:
                        if not self.ballToMakeRadius -1 <= 5:
                            self.ballToMakeRadius -= 1

                    if event.key == pygame.K_LEFT:
                        if not self.ballToMakeElasticity - 0.05 <= 0:
                            self.ballToMakeElasticity = round(self.ballToMakeElasticity - 0.05, 2)
                            print(self.ballToMakeElasticity)
                    elif event.key == pygame.K_RIGHT:
                        self.ballToMakeElasticity = round(self.ballToMakeElasticity + 0.05, 2)

                    # print(self.ballToMakeRadius)
                    # print(self.mouse_move_amount)
            if pygame.mouse.get_pressed()[0] and not self.pressed:
                pygame.mouse.get_rel()
                self.pressed = True
                self.startPos = mousePos
                self.ballToMakeRadius = 10
                self.ballToMakeElasticity = 0.75
                # print("Mouse pressed")
                # print(self.ballToMakeRadius)
                
            if not pygame.mouse.get_pressed()[0] and self.pressed: 
                self.pressed = False
                
                
                self.balls.append(Ball([self.startPos[0], self.startPos[1]], self.ballToMakeRadius, "white", pygame.mouse.get_rel()[1]*-1, self.ballToMakeElasticity, True if self.allOverlaysOff == False else False))
                self.ballToMakeRadius = 10
                self.ballToMakeElasticity = 0.75
                # print("Mouse upressed")

            # if self.dragging:
                

            self.display.fill("black")
            if self.pressed:
                pygame.draw.circle(self.display, "blue", self.startPos, self.ballToMakeRadius)
                self.dragOverlay.draw(mousePos, ("V", (mousePos[1] - self.startPos[1]) * -1))

            # if self.dragging:
            #     self.dragEffect.draw(pygame.mouse.get_pos())
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