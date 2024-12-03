import math, time

class CollisionChecker:

    def correctAndCheckCollision(self, obj1, obj2):
        if self.distance(obj1.pos[0], obj2.pos[0], obj1.pos[1], obj2.pos[1]) < obj1.radius + obj2.radius:
            self.correctCollision(obj1, obj2)
        # return False
    
    def correctCollision(self, obj1, obj2):
        angle = math.atan2(obj2.pos[1] - obj1.pos[1], obj2.pos[0] - obj1.pos[0])
        magnitudes = [self.magnitude(obj1), self.magnitude(obj2)]
        vecAngles = [math.atan2(magnitudes[0] * math.sin(obj1.v[1]),   magnitudes[0] * math.cos(obj1.V0[0])), 
                     math.atan2(magnitudes[0] * math.sin(obj2.v[1]),   magnitudes[0] * math.cos(obj2.V0[0]))]
        # print(vecAngles)
        obj1.V0[0] = magnitudes[0] * math.cos(2 *(vecAngles[0] - angle))
        obj2.V0[0] = magnitudes[1] * math.cos(2 * (vecAngles[1] - angle))

        obj1.v[0] = magnitudes[0] * math.sin(2 *(vecAngles[0] - angle))
        obj2.v[0] = magnitudes[1] * math.sin(2 * (vecAngles[1] - angle))
        times = [time.time(), time.time()]
        obj1.t0 = times
        obj2.t0 = times
        # print(angle * (180/math.pi))

    def distance(self, x1, x2, y1, y2):
        distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
        return distance
    
    def magnitude(self, obj):
        return math.sqrt(math.pow(obj.V0[0], 2) + math.pow(obj.v[1], 2))
    
    # def updateBallList(self, newList):
    #     self.balls = newList