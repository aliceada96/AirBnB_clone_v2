#!/usr/bin/python3
"""This module contains unit tests for the functions and classes defined in the
amenity model """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Tests for Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity model """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests the name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
