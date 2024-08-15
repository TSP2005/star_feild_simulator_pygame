import pygame
import sys
import random
import math

screen_dim = [800, 600]


class StarFieldSimulation:
    def __init__(self):
        pygame.init()
        self.window_dim = screen_dim
        self.screen = pygame.display.set_mode(self.window_dim)
        pygame.display.set_caption("star field simulation")
        self.stars = []
        self.clock = pygame.time.Clock()
        self.FPS = 240

    def render(self):
        for star in self.stars:
            size = 1+((math.sqrt((star.loc[0]-screen_dim[0]/2)**2 + (star.loc[1]-screen_dim[1]/2)**2)/1000) * star.max_size)
            pygame.draw.ellipse(self.screen, star.color, (star.loc[0], star.loc[1], size, size), 0)

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(self.FPS)
            self.render()
            self.update()
            pygame.display.update()

    def update(self):
        for star in self.stars:
            mouse_pos = pygame.mouse.get_pos()
            distance = math.sqrt((star.loc[0]-screen_dim[0]/2)**2 + (star.loc[1]-screen_dim[1]/2)**2)
            speed_factor = math.exp(distance/1000)
            star.loc[0] += (star.loc[0] - (screen_dim[0] - star.loc[0])) * 0.00003 * mouse_pos[0]*speed_factor
            star.loc[1] += (star.loc[1] - (screen_dim[1] - star.loc[1])) * 0.00003 * mouse_pos[0]*speed_factor
            if star.loc[0] < 0 or star.loc[0] > screen_dim[0] or star.loc[1] < 0 or star.loc[1] > screen_dim[1]:
                star.loc = [random.uniform(screen_dim[0]/2-10, screen_dim[0]/2+10), random.uniform(screen_dim[1]/2-10, screen_dim[1]/2+10)]


class Star:
    def __init__(self):
        self.loc = [random.uniform(0, screen_dim[0]), random.uniform(0, screen_dim[1])]
        self.max_size = 20

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.tail = []

    def __repr__(self):
        return f'star(location = {self.loc}, size = {self.max_size})'


if __name__ == "__main__":
    sim = StarFieldSimulation()
    for i in range(3000):
        obj = Star()
        sim.stars.append(obj)
    sim.run()
