#!/usr/bin/python3
"""This module contains unit tests for the functions and classes defined in the
city model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Tests for City Class """

    def __init__(self, *args, **kwargs):
        """Initializes City class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests state attribute"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Tests for name attribute """
        new = self.Svalue()
        self.assertEqual(type(new.name), str)
