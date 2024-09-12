import pygame, time, math
from dataOverlay import OverLay
pygame.init()

class Ball:
    def __init__ (self, pos, radius, color, V0, elasticity, showOverlay):
        self.radius = radius
        self.color = color
        self.display = pygame.display.get_surface()
        self.displayHeight = self.display.get_height()

        self.V0 = V0
        self.elasticity = elasticity
        self.pos = pos
        self.g = -9.8

        self.lastV = V0
        self.scalar = 100
        self.t0 = time.time()
        self.Y0 = pos[1]
        self.showOverlay = showOverlay
        if self.showOverlay:
            self.overlay = OverLay((pos[0], pos[1]), self.color, 10, ("Y", self.pos[1]), ("V", self.V0), self.radius, self.V0)




        # self.stopSimulation = False

        # self.ball_count = ball_count


        # self.font = pygame.font.Font('freesansbold.ttf', 20)
        # self.yText = self.font.render(f"{round(self.Y0, 2)}", True, self.color)
        # self.textRect = self.yText.get_rect()

        # self.yLabel = self.font.render(f"Y:", True, self.color)
        # self.textRect2 = self.yLabel.get_rect()

        

        # self.font = pygame.font.Font('freesansbold.ttf', 10)
        # self.vText = self.font.render(f"{self.V0}", True, self.color)
        # self.textRect3 = self.vText.get_rect()
        # # print(self.textRect3.width)
        # # print(self.textRect3.height)
        

        # self.vLabel = self.font.render(f"V:", True, self.color)
        # self.textRect4 = self.vLabel.get_rect()
        

        # self.TextTotalHeight = (self.textRect.height + 22 + self.textRect4.height) * self.ball_count
        # self.textRect.center = (47, self.TextTotalHeight - 22)
        # self.textRect2.center = (8, self.TextTotalHeight - 22)
        # self.textRect3.center = (47, self.TextTotalHeight - 2)
        # self.textRect4.center = (8, self.TextTotalHeight - 2)


    def move(self, dt):
        t = (time.time() - self.t0)
        # y = self.displayHeight - self.radius
        # v = 0
        # if (not self.stopSimulation):
        y = self.Y0 + self.V0*t - (1/2 * (self.g * self.scalar) * (t**2))
        # v = math.sqrt(self.V0**2 - 2*self.g*(y - self.Y0))
        self.v = self.V0 - (self.g * self.scalar)* t
        # print(v, self.V0)

        
        # if self.radius + y <= self.displayHeight and v >= -1 and v <= 0:
        #     # print("Stop")
        #     self.stopSimulation = True
            # self.V0 = 0

        if self.radius + y >= self.displayHeight:
            self.t0 = time.time()
            self.Y0 = self.displayHeight - self.radius
            y = self.displayHeight - self.radius

                # self.V0 *= 0.85
                # self.V0 = self.V0 - self.g*t
            # if v <= 0:
            #     y += self.radius
            
            self.V0 = (((self.v + self.lastV)/2) * -1) * self.elasticity

            # if y == self.displayHeight - self.radius and math.floor(v) == 0:
            #     self.V0 = 0
            #     print("Hi")
            # y = self.pos[1] + self.V0*t - (1/2 * self.g * (t**2))

        # self.yText = self.font.render(f"{math.floor(y)}", True, self.color)
        # self.vText = self.font.render(f"{math.floor(v)}", True, self.color)
        
        self.pos[1] = y
        self.lastV = self.v
        # print(self.pos)

    def draw(self):
       pygame.draw.circle(self.display, self.color, self.pos, self.radius)
       if self.showOverlay:
        self.overlay.draw(self.pos, ("Y", self.pos[1]), ("V", self.v), self.elasticity)
    #    self.display.blit(self.yText, self.textRect)
    #    self.display.blit(self.yLabel, self.textRect2)
    #    self.display.blit(self.vText, self.textRect3)
    #    self.display.blit(self.vLabel, self.textRect4)

    def update(self, dt):
        self.move(dt)
        self.draw()
    # def update():

# if has_enough_units and has_met_requirements:
#     can_graduate = True
# else:
#     can_graduate = False