import pygame, time, math
from dataOverlay import OverLay
pygame.init()

class Ball:
    def __init__ (self, pos: list, radius: int, color: str, V0: list, elasticity: float, showOverlay: bool):
        self.radius = radius
        self.color = color
        self.display = pygame.display.get_surface()
        self.displayHeight = self.display.get_height()

        self.V0 = V0.copy()
        self.elasticity = elasticity
        self.pos = pos
        # self.g = 0
        self.g = -9.8
        self.a = 0
        
        self.lastV = V0.copy()
        self.scalar = 100
        self.t0 = time.time()
        self.Pos0 = pos.copy()
        # print(self.Pos0)
        self.showOverlay = showOverlay
        self.v = V0.copy()
        # if self.showOverlay:
        self.overlay = OverLay((pos[0], pos[1]), self.color, 10, ("Y", self.pos[1]), ("VY", self.V0[1]), self.radius, self.V0[1])
        # print(self.lastV, self.V0, self.v)


    def move(self, dt):
        t = time.time() - self.t0
        # y = self.displayHeight - self.radius
        # v = 0
        # if (not self.stopSimulation):
        y = self.Pos0[1] + self.V0[1]*t - (1/2 * (self.g * self.scalar) * (t**2))
        x = self.Pos0[0] + self.V0[0]*t 
        # print(x, self.Pos0[0], self.V0[0])

        
        # print(self.Pos0)

        # v = math.sqrt(self.V0**2 - 2*self.g*(y - self.Y0))
        # print(self.lastV, self.V0)
        # print(self.V0[1])
        # print(t)
        self.v[1] = self.V0[1] - (self.g * self.scalar)* t
        # self.v[0] = (self.v[0] + self.V0[0])/2
        self.v[0] = (x - self.Pos0[0]) / t if t != 0 else 1

        # print(self.v)
        # print(self.V0[1] - (self.g * self.scalar) * t)
        # print(self.v[1])
        # print(self.v[1], self.lastV[1])
        # print(v, self.V0)

        
        # if self.radius + y <= self.displayHeight and v >= -1 and v <= 0:
        #     # print("Stop")
        #     self.stopSimulation = True
            # self.V0 = 0
        # print(y)
        if self.radius + y >= self.displayHeight:
            self.t0 = time.time()
            # print(self.Pos0)
            self.Pos0[1] = self.displayHeight - self.radius
            self.Pos0[0] = x
            y = self.displayHeight - self.radius
            
            # print(self.lastV, self.v, self.V0)
            # print(f"Average {((self.v[1] + self.lastV[1])/2) * -1}")
            self.V0[1] = ((((self.v[1] + self.lastV[1])/2) * -1) * self.elasticity)
            self.V0[0] = self.v[0] * self.elasticity
        
        if x - self.radius < 0:
            self.V0[0] = (((self.v[0] + self.lastV[0])/2) * -1) * self.elasticity
            x = self.radius
            self.Pos0[0] = x
            print("HIT LEFT")
            # self.Pos0[0] = x
        elif x + self.radius > self.display.get_width():
            # self.V0[0] = (((self.v[0] + self.lastV[0])/2) * -1)
            self.V0[0] = (self.v[0] * -1)
            x = self.display.get_width() - self.radius
            self.Pos0[0] = x
            print(x)
            print("HIT RIGHT")
        
        self.pos[1] = y
        self.pos[0] = x
        # print(self.pos)

        self.lastV = self.v.copy()


    def draw(self):
       pygame.draw.circle(self.display, self.speed_to_color(), self.pos, self.radius)
       if self.showOverlay:
        self.overlay.draw(self.pos, ("Y", self.pos[1]), ("VY", self.v[1]), self.elasticity)
    #    self.display.blit(self.yText, self.textRect)
    #    self.display.blit(self.yLabel, self.textRect2)
    #    self.display.blit(self.vText, self.textRect3)
    #    self.display.blit(self.vLabel, self.textRect4)

    def speed_to_color(self):
        intensity = min(255, int((abs(self.v[1]) / 1000) * 255))
        return (intensity, 0, 255 - intensity)

    def update(self, dt):
        self.move(dt)
        self.draw()
    # def update():

# if has_enough_units and has_met_requirements:
#     can_graduate = True
# else:
#     can_graduate = False