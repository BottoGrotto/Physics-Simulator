import pygame, math
pygame.init()

class DragEffect:
    def __init__(self, radius, color, distance, mouseStart):
        self.display = pygame.display.get_surface()
        self.radius = radius
        self.color = color
        self.distance = distance
        self.current_distance = 0

        self.initalMouse = (0, 0)

        self.start = mouseStart
        self.ballsPos = []

    # def createBall(self, pos):
        # self.balls.append(pygame.)


    def draw(self, mousePos):
        
        # if len(self.ballsPos) > 2:
        #     if mousePos[1] >= self.ballsPos[-1][1] + self.ballsPos[-2][1]:
        #         self.ballsPos.append(mousePos)
        # else:
        #     self.ballsPos.append(mousePos)
        for ball in self.ballsPos:
            pygame.draw.circle(self.display, self.color, (self.start[0], ball[1]), self.radius)
