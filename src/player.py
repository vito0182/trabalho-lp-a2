import pygame as pg
from utils import load_image

class Entity(pg.sprite.Sprite):
    """
    Generic class to represent any entity. An entity is something that have a
    sprite and can move within the map.

    Parameters
    ----------
    image_path:
        A tuple containing the directory names leading to the entity image.
    initial_position:
        The position where the entity should be when created. Defaults to (0, 0).
    """
    def __init__(self, image_path, initial_position = (0, 0)):
        super().__init__()
        self.image = load_image(image_path)
        self.rect = self.image.get_rect(topleft = initial_position)
        self.direction = pg.math.Vector2()

class Player(Entity):
    """
    Class representing the player. It implements some functions that are used
    to move the player based on keyboard inputs.

    Parameters
    ----------
    image_path:
        A tuple containing the directory names leading to the player image.
    initial_position:
        The position where the entity should be when created. Defaults to (0, 0).
    map_size:
        The map size. It is used to determine when the player is on the map edge.
    """
    def __init__(self, image_path, initial_position, map_size):
        super().__init__(image_path, initial_position)
        self.speed = 10
        self.map_size = map_size

    def update(self):
        self.get_input()
        if self.direction.magnitude_squared() != 0:
           self.move(self.speed)

    def get_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] and not keys[pg.K_DOWN]:
            self.direction.y = -1
        elif keys[pg.K_DOWN] and not keys[pg.K_UP]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pg.K_RIGHT] and not keys[pg.K_LEFT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT] and not keys[pg.K_RIGHT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        if self.rect.x > self.map_size[0]:
            self.rect.x -= self.map_size[0]
        elif self.rect.x < 0:
            self.rect.x += self.map_size[0]

        self.rect.y += self.direction.y * speed
        if self.rect.y > self.map_size[1]:
            self.rect.y -= self.map_size[1]
        elif self.rect.y < 0:
            self.rect.y += self.map_size[1]
        #print(self.rect)
