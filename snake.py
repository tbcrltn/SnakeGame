import pygame
class Snake:
    def __init__(self, size, speed, screen):
        self.size = size
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.screen = screen
        self.snake = None
        self.x = 300 - self.size/2
        self.y = 300 - self.size/2
        

    def update(self):
        half_size = self.size/2
        self.snake = pygame.draw.rect(self.screen, (0, 0, 200), (self.x, self.y, self.size, self.size))
        self.move()
        self.check_growth()
        self.check_collision()

    def move(self):
        self.dx, self.dy = self.get_movement_values()
        self.x += self.dx
        self.y += self.dy

    def get_movement_values(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.dy == 0:
                return 0, -self.speed
            else: return self.dx, self.dy
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.dy == 0:
                return 0, self.speed
            else: return self.dx, self.dy
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.dx == 0:
                return self.speed, 0
            else: return self.dx, self.dy
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.dx == 0:
                return -self.speed, 0
            else: return self.dx, self.dy
        
        else: return self.dx, self.dy



    def check_growth(self):
        pass

    def check_collision(self):
        pass