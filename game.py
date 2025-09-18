import pygame
from snake import Snake
class Game:
    def __init__(self, winh, winw):
        self.screen = pygame.display.set_mode((winh, winw))
        self.__running = True
        self.snake = Snake(15, 2, self.screen)


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
        

    def check_window_closure(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False