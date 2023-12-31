"""
This module have functions that doesn't fit in any class, but are used along
all the code. They easen processes like loading images.
"""
from settings import TILE_SIZE, PX_SCALE

import pygame as pg

import math
import json
from os.path import join

def load_tile_image(image_path):
    """
    Loads an image from a file and scales it to the size of a tile.

    Parameters
    ----------
    image_path: tuple
        A tuple with the path to the file. This is to prevent OS issues.

    Returns
    -------
    pg.Surface
        A surface with the loaded image
    """
    image = pg.image.load(join(*image_path))
    image = image.convert_alpha()
    image = pg.transform.scale(image, (TILE_SIZE, TILE_SIZE))
    return image

def load_image(image_path, scale = PX_SCALE):
    """
    Loads an image from a file and scales it by a factor of scale.

    Parameters
    ----------
    image_path: tuple
        A tuple with the path to the file. This is to prevent OS issues.
    scale: Optional(int)
        The number that should be used to scale the image

    Returns
    -------
    pg.Surface
        A surface with the loaded image
    """
    image = pg.image.load(join(*image_path))
    image = image.convert_alpha()
    image_height = image.get_height()
    image_width = image.get_width()
    image = pg.transform.scale(image, (image_width * scale, image_height * scale))
    return image

def load_map(filepath):
    """
    Loads a map from a json file.

    Parameters
    ----------
    image_path: tuple
        A tuple with the path to the file. This is to prevent OS issues.

    Returns
    -------
    list
        A list of lists, with the data layout information.
    """
    with open(filepath, 'r') as file:
        map_layout = json.load(file)
    return map_layout

def angle_to(sprite1, sprite2):
    """
    Returns the angle (in radians) between two sprites.

    Parameters
    ----------
    sprite1: pg.Sprite
        The first sprite to compare angles.
    sprite2: pg.Sprite
        The second sprite to compare angles.

    Returns
    -------
    float
        The angle value in radians
    """
    x1, y1 = sprite1.rect.center
    x2, y2 = sprite2.rect.center
    return math.atan2(y1 - y2, x1 - x2)

def image_clip(surface, x, y, x_size, y_size):
    """
    Returns a clipped image from a surface.
    
    Parameters
    ----------

    surface: pygame.Surface
        The surface to be clipped.
    x: int
        The x coordinate of the top left corner of the clipped image.
    y: int
        The y coordinate of the top left corner of the clipped image.
    x_size: int
        The width of the clipped image.
    y_size: int
        The height of the clipped image.

    Returns
    -------

    image: pygame.Surface
        The clipped image.
    """
    image_copy = surface.copy()
    clip = pg.Rect(x, y, x_size, y_size)
    image_copy.set_clip(clip)
    image = surface.subsurface(image_copy.get_clip())
    return image.copy()

def draw_text(text:str, font:pg.font.Font, color:tuple, surface:pg.Surface, x:int, y:int):
    """
    Draws text on a surface.

    Parameters
    ----------
    text: str
        The text to be drawn.
    font: pygame.font.Font
        The font to be used.
    color: tuple
        The color of the text.
    surface: pygame.Surface
        The surface where the text will be drawn.
    x: int
        The x coordinate of the center of the text.
    y: int
        The y coordinate of the center of the text.
    """
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)
