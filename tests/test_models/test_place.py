#!/usr/bin/python3
"""This module contains unit tests for the functions and classes defined in the
place model"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Defines tests for Place"""

    def __init__(self, *args, **kwargs):
        """Defines tests for init method"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Defines tests for city_id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Defines tests for user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Defines tests for nam attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Defines tests for description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Defines tets for number_rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Defines tests for number_bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Defines tests for max_guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Defines tests for price_by_night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Defines tests for lattitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Defines tests for longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Defines tests for amenity"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
