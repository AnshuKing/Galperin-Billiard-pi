import pygame
from pygame.locals import*
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption ("|PI|")
screen.fill((255,255,255))
clacks = 0
font = pygame.font.SysFont("Somic Sans MS", 20)
digits = 2
time_steps = 1000



    
    
class Block:
    def __init__(self, x, w,v, m):
        self.x = x
        self.w = w
        self.v = v
        self.m = m
    def update(self):
        self.x+= self.v

    def collision(self, other):
        if ((self.x+self.w)<other.x) or (self.x>(other.x+other.w)):
            return False
        else:
            return True
    def bounce(self, other):
        sum_m = (self.m+other.m)
        new_vel = ((self.m-other.m)/sum_m * self.v ) + (2*other.m/sum_m * other.v) #Elastic collision formula
        return new_vel
    def hit_wall(self):
        global clacks
        if self.x<=0:
            self.v*= -1
            clacks+=1
    def show(self):
        self.block = pygame.draw.rect(screen,(255,0,0),(self.x, 400-self.w-1,self.w, self.w))
        





crashed = False
b1 = Block(600,100,-5/time_steps, 100**digits)
b2 = Block(200,30,0,1)
while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True
    for i in range(0, time_steps):
        if (b1.collision(b2)):
            clacks+=1
            v1 = b1.bounce(b2)
            v2 = b2.bounce(b1)
            b1.v = v1
            b2.v = v2
        b2.hit_wall()
        b1.update()
        b2.update()
    b1.show()
    b2.show()
    pygame.draw.rect(screen,(20,20,20),(0,400,800,500))
    text = font.render("Collisions: "+str(clacks), True, (20, 20, 20))
    screen.blit(text,(0, 00))
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(60)#Frame Rate
   
    screen.fill((255,255,255))


pygame.quit()
print(clacks)
