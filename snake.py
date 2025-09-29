import pygame
class Snake:
    def __init__(self, size, speed, screen, growth):
        self.size = size
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.screen = screen
        half_size = self.size /2
        self.x = 300 - half_size
        self.y = 300 - half_size
        self.snake = pygame.Rect(self.x -half_size, self.y-half_size, self.size, self.size)
        self.segments = []
        self.segments.append(self.snake)
        self.dir = None
        self.growth_length = growth
        self.snake_length = 3
        

    def update(self):
        for segment in self.segments:
            pygame.draw.rect(self.screen, (0, 0, 200), segment)
        self.move()
        self.check_collision()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dir = "u"
        elif keys[pygame.K_DOWN]:
            self.dir = "d"
        elif keys[pygame.K_LEFT]:
            self.dir = "l"
        elif keys[pygame.K_RIGHT]:
            self.dir = "r"


        head = self.segments[0].copy()

        if self.dir == "u":
            head.y -= self.speed
        elif self.dir == "d":
            head.y += self.speed
        elif self.dir == "l":
            head.x -= self.speed
        elif self.dir == "r":
            head.x += self.speed

        self.segments.insert(0, head)

        if len(self.segments) > self.snake_length:
            self.segments.pop()
            
            




    def grow(self):
        self.snake_length += self.growth_length

    def check_collision(self):
        pass

    def get_rects(self):
        half_size = self.size/2
        return self.segments[0]