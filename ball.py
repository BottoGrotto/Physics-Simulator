import pygame, time, math
pygame.init()

class Ball:
    def __init__ (self, pos, radius, color, initalVelocity=0):
        self.radius = radius
        self.color = color
        self.display = pygame.display.get_surface()
        self.V0 = initalVelocity
        self.pos = pos
        self.g = -9.8
        self.scalar = 100
        self.t0 = time.time()
        self.Y0 = pos[1]
        self.displayHeight = self.display.get_height()


        self.font = pygame.font.Font('freesansbold.ttf', 10)
        self.yText = self.font.render(f"{round(self.Y0, 2)}", True, "green")
        self.textRect = self.yText.get_rect()
        self.textRect.center = (self.textRect.width+ 4, 10)

        self.yLabel = self.font.render(f"Y:", True, "green")
        self.textRect2 = self.yLabel.get_rect()
        self.textRect2.center = (5, 10)

        self.font = pygame.font.Font('freesansbold.ttf', 10)
        self.vText = self.font.render(f"{self.V0}", True, "green")
        self.textRect3 = self.vText.get_rect()
        self.textRect3.center = (self.textRect3.width + 10, 22)

        self.vLabel = self.font.render(f"V:", True, "green")
        self.textRect4 = self.vLabel.get_rect()
        self.textRect4.center = (5, 22)
        

    def move(self, dt):
        t = (time.time() - self.t0)
        y = self.Y0 + self.V0*t - (1/2 * (self.g * self.scalar) * (t**2))
        # v = math.sqrt(self.V0**2 - 2*self.g*(y - self.Y0))
        v = self.V0 - (self.g * self.scalar)* t
        print(v, self.V0)

        
        if self.radius + y >= self.displayHeight:
            self.t0 = time.time()
            self.Y0 = self.displayHeight - self.radius
            y = self.displayHeight - self.radius
                # self.V0 *= 0.85
                # self.V0 = self.V0 - self.g*t
            # if v <= 0:
            #     y += self.radius
            
            self.V0 = (v * -1) * 0.75
            # if y == self.displayHeight - self.radius and math.floor(v) == 0:
            #     self.V0 = 0
            #     print("Hi")
            # y = self.pos[1] + self.V0*t - (1/2 * self.g * (t**2))

        self.yText = self.font.render(f"{round(y, 2)}", True, "green")
        self.vText = self.font.render(f"{round(v, 2)}", True, "green")
        self.pos[1] = y
        # print(self.pos)

    def draw(self):
       pygame.draw.circle(self.display, self.color, self.pos, self.radius)
       self.display.blit(self.yText, self.textRect)
       self.display.blit(self.yLabel, self.textRect2)
       self.display.blit(self.vText, self.textRect3)
       self.display.blit(self.vLabel, self.textRect4)

    def update(self, dt):
        self.move(dt)
        self.draw()
    # def update():

# if has_enough_units and has_met_requirements:
#     can_graduate = True
# else:
#     can_graduate = False