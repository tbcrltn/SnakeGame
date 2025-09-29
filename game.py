import pygame
import random
from snake import Snake
class Game:
    def __init__(self, winh, winw):
        self.screen = pygame.display.set_mode((winh, winw))
        self.__running = True
        self.snake = Snake(15, 2, self.screen, 10)
        self.fruit = None
        self.fruit_x = 400
        self.fruit_y = 300
        self.fruit_size = 8
        self.score = 0


    def start_game(self):
        while self.__running:
            self.check_window_closure()
            self.mainloop()
            pygame.time.Clock().tick(60)
            pygame.display.update()
        pygame.quit()

    def mainloop(self):
        self.screen.fill((0, 150, 0))
        self.snake.update()
        self.update_fruit()
        

    def check_window_closure(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

    def update_fruit(self):
        self.fruit = pygame.draw.circle(self.screen, (200, 0, 0), (self.fruit_x, self.fruit_y), self.fruit_size)
        fruit_rect = pygame.Rect(self.fruit.centerx - self.fruit_size, self.fruit.centery - self.fruit_size, self.fruit_size * 2, self.fruit_size * 2)
        snake_rects = self.snake.get_rects()
        if fruit_rect.colliderect(snake_rects):
            self.fruit_x = random.randint(20, 580)
            self.fruit_y = random.randint(20, 580)
            self.addscore(1)
            self.snake.grow()

    def addscore(self, num):
        self.score += num
