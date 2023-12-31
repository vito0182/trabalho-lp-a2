"""
This module have a class representing a cursor. The cursor have some usefull
properties that are used when aiming to something, when centering the camera
and so on.
"""
from utils import load_image

import pygame as pg


class Cursor:
    """
    This class represents the cursor object in the game.
    """

    def __init__(self, image_path: str, initial_position: tuple):
        """
        Args:
            image_path (str): Path to the image file for the cursor.
            initial_position (tuple): Initial position of the cursor.y
        """
        self._image = load_image(image_path)
        self._rect = self._image.get_rect(center=initial_position)
        self._angle_radians = 0
        self._angle_degrees = 0

    @property
    def image(self) -> pg.Surface:
        """
        Returns the pygame Surface object of the cursor image.
        """
        return self._image

    @property
    def rect(self) -> pg.Rect:
        """
        Returns the pygame Rect object of the cursor's position and size.
        """
        return self._rect

    def set_image(self, image_path) -> pg.Surface:
        """
        Returns the pygame Surface object of the cursor image.
        """
        self._image = load_image(image_path)

    def update(self):
        """
        Updates the position of the cursor, using the mouse position

        Returns
        -------
        None
        """
        self._rect.center = pg.mouse.get_pos()
