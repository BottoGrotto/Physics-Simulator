import pygame, time, math
from dataOverlay import OverLay
pygame.init()

class Ball:
    def __init__ (self, pos: list, radius: int, color: str, V0: list, elasticity: float, showOverlay: bool, Sfriction: float, Kfriction: float, mass: float):
        self.radius = radius
        self.color = color
        self.display = pygame.display.get_surface()
        self.displayHeight = self.display.get_height()

        self.V0 = V0.copy()
        self.elasticity = elasticity
        self.Sfriction = Sfriction
        self.Kfriction = Kfriction
        self.pos = pos
        self.g = -9.8
        self.mass = mass
        
        self.lastV = V0.copy()
        self.scalar = 100
        self.t0 = [time.time(), time.time()]
        self.Pos0 = pos.copy()

        self.showOverlay = showOverlay
        self.v = V0.copy()

        self.magnitude = self.calculateMagnitude()

        # if self.showOverlay:
        self.overlay = OverLay((pos[0], pos[1]), self.color, 10, ("Y", self.pos[1]), ("VY", self.V0[1]), self.radius, round(self.magnitude, 2))
        # print(self.lastV, self.V0, self.v)


    def move(self, dt):
        t = time.time()
        tx = t - self.t0[0]
        ty = t - self.t0[1]
        y = self.Pos0[1] + self.V0[1]*ty - (1/2 * (self.g * self.scalar) * (ty**2))
        x = self.Pos0[0] + self.V0[0]*tx 
        # print(x, self.Pos0[0], self.V0[0], t)

        
        # print(self.Pos0)

        # v = math.sqrt(self.V0**2 - 2*self.g*(y - self.Y0))
        # print(self.lastV, self.V0)
        # print(self.V0[1])
        # print(t)
        self.v[1] = self.V0[1] - (self.g * self.scalar)* ty
        # self.v[0] = (self.v[0] + self.V0[0])/2
        # self.v[0] = (x - self.Pos0[0]) / t if t != 0 else 0.01
        
        
        if self.radius + y >= self.displayHeight:
            t = time.time()
            self.t0[1] = t
            self.t0[0] = t
            # print(self.Pos0)
            self.Pos0[1] = self.displayHeight - self.radius
            self.Pos0[0] = x
            y = self.displayHeight - self.radius
            
            # print(self.lastV, self.v, self.V0)
            # print(f"Average {((self.v[1] + self.lastV[1])/2) * -1}")
            self.V0[1] = ((((self.v[1] + self.lastV[1])/2) * -1) * self.elasticity)
            # self.V0[0] = self.v[0] * self.friction
            # fg = (self.mass * self.g * self.scalar)
            # fa = -(self.mass * self.v[1])/t
            # # print(fg, round(fa, 1))
            # fn = fg
            # f = (self.mass * self.v[0])/t

            # ff = (self.Kfriction * fn)
            # print(f, self.Kfriction * fn)
            # f = self.v[0]
            # print(ff, f)
            # print(f + ff)
            # fnet = f - ff 
            # # print(ff)
            # if fnet == 0:
            #     self.v[0] = 0
            # self.v[0] = (fnet*t/self.mass)
            self.V0[0] = self.V0[0] * self.Kfriction
            self.v[0] = self.v[0] * self.Kfriction

            # print(self.v[0],  ((self.mass * self.v[0])/t), t)
            # self.V0[0] = self.v[0] * 

        if x - self.radius < 0:
            # print(x, self.Pos0[0], t)
            self.t0[0] = time.time()
            # pygame.time.delay(500)
            # self.t0 = time.time()
            # print(self.V0[0])
            # self.V0[0] = (((self.v[0] + self.lastV[0])/2) * -1)
            # self.V0[0] = self.v[0] * -1
            # print(self.V0[0])
            self.V0[0] *= -1
            self.v[0] *= -1
            # x = self.radius
            # print(x, x - self.radius < 0) 

            self.Pos0[0] = self.radius
            # print("HIT LEFT")
            # time.sleep(1)
            # self.Pos0[0] = x
        elif x + self.radius > self.display.get_width():
            self.t0[0] = time.time()
            # self.t0 = time.time()
            # self.V0[0] = (((self.v[0] + self.lastV[0])/2) * -1)
            # self.V0[0] = (self.v[0] * -1)
            pos = self.display.get_width() - self.radius
            # x = pos
            self.Pos0[0] = pos
            self.V0[0] *= -1
            self.v[0] *= -1
            # print(x)
            # print("HIT RIGHT")
        
        self.pos[1] = y
        self.pos[0] = x
        # print(self.pos)

        self.lastV = self.v.copy()


    def draw(self):
       pygame.draw.circle(self.display, self.speed_to_color(), self.pos, self.radius)
       if self.showOverlay:
        self.overlay.draw(self.pos, ("Y", self.pos[1]), ("VY", self.v[1]), self.elasticity)

    def speed_to_color(self):
        self.magnitude = self.calculateMagnitude()
        intensity = min(255, int((abs(self.magnitude) / 1000) * 255))
        return (intensity, 0, 255 - intensity)
    
    def calculateMagnitude(self):
        return math.sqrt((self.v[0]**2) + (self.v[1]**2))
    
    

    def update(self, dt):
        self.move(dt)
        self.draw()